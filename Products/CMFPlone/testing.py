from Acquisition import aq_base
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework import AutoLogin
from plone.app.robotframework import Content
from plone.app.robotframework import RemoteLibraryLayer
from plone.app.testing import login
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing.layers import IntegrationTesting
from plone.app.z3cform.widgets.select import Select2Widget
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from plone.testing import zope
from Products.CMFPlone.tests.robot.robot_setup import CMFPloneRemoteKeywords
from Products.CMFPlone.tests.utils import MockMailHost
from Products.MailHost.interfaces import IMailHost
from z3c.form import form
from zope.component import getSiteManager
from zope.configuration import xmlconfig
from zope.interface import Interface
from zope.schema import Choice
from zope.schema import List

import doctest


class ProductsCMFPloneLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import Products.CMFPlone

        xmlconfig.file(
            "configure.zcml", Products.CMFPlone, context=configurationContext
        )
        xmlconfig.file(
            "configure.zcml", Products.CMFPlone.tests, context=configurationContext
        )

    def setUpPloneSite(self, portal):
        portal.acl_users.userFolderAddUser("admin", TEST_USER_PASSWORD, ["Manager"], [])
        login(portal, "admin")
        portal.portal_workflow.setDefaultChain("simple_publication_workflow")
        setRoles(portal, TEST_USER_ID, ["Manager"])
        portal.invokeFactory("Folder", id="test-folder", title="Test Folder")
        # XXX: this is needed for tests that rely on the Members folder to be
        # present. This folder is otherwise created by a setup handler in
        # ATContentTypes, but that package is optional now.
        if "Members" not in portal.keys():
            portal.invokeFactory("Folder", id="Members", title="Members")

        portal._original_MailHost = portal.MailHost
        mail_host = MockMailHost("MailHost")
        mail_host.smtp_host = "localhost"
        portal.MailHost = mail_host
        site_manager = getSiteManager(portal)
        site_manager.unregisterUtility(provided=IMailHost)
        site_manager.registerUtility(mail_host, IMailHost)

    def tearDownPloneSite(self, portal):
        login(portal, "admin")
        setRoles(portal, TEST_USER_ID, ["Manager"])
        portal.manage_delObjects(["test-folder"])

        portal.MailHost = portal._original_MailHost
        sm = getSiteManager(context=portal)
        sm.unregisterUtility(provided=IMailHost)
        sm.registerUtility(aq_base(portal._original_MailHost), provided=IMailHost)


PRODUCTS_CMFPLONE_FIXTURE = ProductsCMFPloneLayer()

PRODUCTS_CMFPLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODUCTS_CMFPLONE_FIXTURE,), name="CMFPloneLayer:Integration"
)
PRODUCTS_CMFPLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRODUCTS_CMFPLONE_FIXTURE,), name="CMFPloneLayer:Functional"
)

PRODUCTS_CMFPLONE_ROBOT_REMOTE_LIBRARY_FIXTURE = RemoteLibraryLayer(
    bases=(PLONE_FIXTURE,),
    libraries=(AutoLogin, Content, CMFPloneRemoteKeywords),
    name="CMFPloneRobotRemoteLibrary:RobotRemote",
)

PRODUCTS_CMFPLONE_ROBOT_TESTING = FunctionalTesting(
    bases=(
        PRODUCTS_CMFPLONE_FIXTURE,
        PRODUCTS_CMFPLONE_ROBOT_REMOTE_LIBRARY_FIXTURE,
        zope.WSGI_SERVER_FIXTURE,
    ),
    name="CMFPloneLayer:Acceptance",
)


class ProductsCMFPloneDistributionsLayer(ProductsCMFPloneLayer):
    defaultBases = (PRODUCTS_CMFPLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import Products.CMFPlone

        xmlconfig.file(
            "configure-distributions.zcml",
            Products.CMFPlone.tests,
            context=configurationContext,
        )

    def setUpPloneSite(self, portal):
        # ProductsCMFPloneLayer already does enough setup.
        pass


PRODUCTS_CMFPLONE_DISTRIBUTIONS_FIXTURE = ProductsCMFPloneDistributionsLayer()

PRODUCTS_CMFPLONE_DISTRIBUTIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODUCTS_CMFPLONE_DISTRIBUTIONS_FIXTURE,),
    name="CMFPloneLayer:DistributionsIntegration",
)

optionflags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE


class ITestSelectWidgetSchema(Interface):

    directives.widget("select_field", Select2Widget)
    select_field = Choice(
        title="Select Widget",
        values=[
            "one",
            "two",
            "three",
        ],
    )

    directives.widget("list_field", Select2Widget)
    list_field = List(
        title="Select Multiple Widget",
        value_type=Choice(
            values=[
                "four",
                "five",
                "six",
            ]
        ),
    )


class TestSelectWidgetForm(AutoExtensibleForm, form.EditForm):

    schema = ITestSelectWidgetSchema
    ignoreContext = True
