Historical release notes
========================

This contains the changelogs from older releases.
Note that there are large gaps, for example there is nothing between 4.3.3 and 5.0.0.
So the value of this historical record is currently doubtful.

For what's new in the current release, see CHANGES.txt.


5.2.2 (2020-08-16)
------------------

Bug fixes:


- Release Plone 5.2.2 final.
  No changes with last release candidate, except that the versions will contain Products.isurlinportal 1.1.0 with a minor security hardening fix.
  [maurits] (#3510)


5.2.2rc3 (2020-08-16)
---------------------

Bug fixes:


- Return a Zope aware engine for page templates based on ``zope.pagetemplate`` instead of ``Products.PageTemplates``.
  Fixes possible problems with such templates, for example z3c.form ones, with Zope 4.4 and higher.
  See `issue 3141 <https://github.com/plone/Products.CMFPlone/issues/3141>`_.
  [maurits] (#3141)
- Depend on new package ``Products.isurlinportal``.
  This contains the ``isURLInPortal`` method that was split off from our ``URLTool``.
  See `issue 3150 <https://github.com/plone/Products.CMFPlone/issues/3150>`_.
  [maurits] (#3150)
- Redirection view: refactor our navigation root editing to a separate method ``edit_for_navigation_root``.
  Since Plone 5.2 the redirectiontool respects INavigationroot:
  with a manual redirect you cannot enter a path starting with ``/`` which 'escapes' the NavigationRoot to the SiteRoot to link to another part of the Plone instance.
  This refactor makes it possible to override this method to return the redirection unchanged, bringing back the pre Plone 5.2 behavior of the ``Products.RedirectionTool`` add-on.
  [maurits] (#3153)
- Control panel configlets: first check visibility, then check condition.
  Visibility is cheaper to check.
  Also fixes `bug 3154 <https://github.com/plone/Products.CMFPlone/issues/3154>`_.
  [maurits] (#3154)


5.2.2rc2 (2020-07-17)
---------------------

Bug fixes:


- Fix an issue in mail_password_template.pt in the message showing the ip to really try the request.REMOTE_ADDR variable if request.HTTP_X_FORWARDED_FOR is empty (when you're not behind apache or nginx).
  [vincentfretin] (#2949)
- mail_password form: Do not crash if the userid is not provided or the user doesn't have an email configured
  [frapell] (#3008)


5.2.2rc1 (2020-06-28)
---------------------

New features:


- Image caption support
  Allow ``figcaption`` in rich text editor as a valid tag.
  Add registry setting for plone.image_caption outputfilter transform.
  [thet] (#2887)
- Add markdown extension settings to markup control panel.
  [thomasmassmann] (#3076)
- Insert virtual custom.css bundle into the header after diazo bundle.
  Only add this when custom css is set in the theming control panel.
  [MrTango] (#3086)


Bug fixes:


- Change control panel item sorting and sort them by title
  [erral] (#721)
- Update HTMLFilter settings to enable TinyMCE styling features. See #2329, #2482, #2535
  [petschki] (#2482)
- If 'tinymce-content-css' option is missing in themes manifest.cfg prevent unnecessary loading of a css at nav_root_url while editing a page.  [krissik] (#2861)
- Redirect (when possible) also ajax requests and do not return an useless body
  [ale-rt] (#3014)
- Merge Hotfix20200121 Check of the strength of password could be skipped. (#3021)
- Merge Hotfix20200121: isURLInPortal could be tricked into accepting malicious links. (#3021)
- Improve tests for the workflow tool method listWFStatesByTitle (#3032)
- Fix index_html on PortalRoot: ReplaceableWrapper did not work.
  [jensens] (#3060)
- Allow accessing ``plone_view.patterns_settings``.
  This was no problem until now, but a newer ``Zope/zope.tales/Chameleon``  is rightly stricter.
  [maurits] (#3066)
- Fix Python 3.8 ``time.clock`` removal in CatalogTool [jensens] (#3082)
- Fixed TypeError when adding both a group and a user to a group.
  [maurits] (#3084)
- Make the resource registry scripts output more robust when a bundle resource is missing. This prevents
  breaking your whole Plone site and access to the resource registry control panel after inserting
  one missing resource.
  [fredvd] (#3096)
- Bugfix for #3103
  [petschki] (#3105)
- Fixed saving ignored exception types in Python 3.  [maurits] (#3115)


5.2.1 (2020-01-13)
------------------

New features:


- Add plone.staticresources to list of addons which are automatically upgraded if upgrade steps are available.
  [thet] (#2976)


Bug fixes:


- fix creation of Plone site not adding default Dexterity content types if example content not explicitly selected by user.
  [ericof] (#1318)
- fix default value for email msgid
  [erral] (#2790)
- Fix: PasswordResetView::getErrors is called, this ensures password is validated through RegistrationTool before attempting to reset password.
  [nazrulword] (#2917)
- Breadcrumbs: consider hidden folders when creating urls [ksuess] (#2935)
- Add Collection to the default_page_types list
  [erral] (#2956)
- Fix localization of "Site setup" in some control panels [vincentfretin] (#2958)
- Fix TTW Bundle compilation broken.
  [thet] (#2969)
- Do not save type settings in "content-controlpanel" when switching between types.
  [cekk] (#2986)
- Correctly fire events when user autologin after the password has been reset.
  [ericof] (#2993)


5.2.0 (2019-07-10)
------------------

Bug fixes:


- Don't activate all sorting tabs when no sort option has been chosen.
  [gyst, rodfersou, jensens] (#1789)
- Fix test failures exposed in Python 3.8
  [pbauer] (#2903)


5.2rc5 (2019-06-27)
-------------------

New features:


- Add support for Python 3.8 [pbauer] (#2896)


Bug fixes:


- Add missing i18n:translate calls
  [erral] (#2891)
- Fix login-help layout on mobile.
  [jensens] (#2893)


5.2rc4 (2019-06-20)
-------------------

New features:


- Remove verifydb, it was moved to standalone package zodbverify.
  [jensens] (#2858)


Bug fixes:


- If specified in the registry, let the user autologin after the password has been reset (#2439)
- Allow empty ``default_page`` registry setting
  [petschki] (#2813)
- Always add ``data-default-sort`` attribute to search results.  [maurits] (#2854)
- Fix deprecation warnings.
  [jensens] (#2862)
- Use the shared 'Plone test setup' and 'Plone test teardown' keywords in Robot tests.
  [Rotonen] (#2864)
- Fix script resource parsing error because of self closing tags.
  [Netroxen] (#2870)


5.2rc3 (2019-05-04)
-------------------

New features:


- Allow filtering on date and manual/automatic in redirection controlpanel. (#2799)
- Add a button to export the alternative urls in redirection controlpanel. (#2799)
- Add a button to remove all alternative urls that match the filter.
  See `issue 2799 <https://github.com/plone/Products.CMFPlone/issues/2799>`_.
  [maurits] (#2799)


Bug fixes:


- gracefully handle tracebacks during addon installation
  [petschki] (#2228)
- Add workaround for the case when a infinite recursion in a page-template that uses the main-template crashes the instance instead of raising a RecursionError.
  [pbauer, esteele] (#2666)
- Fixed unstable Markup Control Panel robot test again.  [maurits] (#2809)
- add a missing space in an error message in the redirects control panel and replace a typo [vincentfretin] (#2821)
- Fixes: Cooking resources with non ASCII resulted in encoding error.
  Further, writing legacy resources resulted in ValueError. [jensens] (#2827)
- restore ``exclude_from_nav`` combined with ``show_excluded_items`` handling
  [petschki] (#2828)
- Fix DeprecationWarning in syndication-view. [jensens] (#2831)
- Fix malformed url when redirecting to external login. [ericof] (#2842)
- Make navigation (CatalogNavigationTabs) subclassing easier. [iham] (#2849)


5.2rc2 (2019-03-21)
-------------------

Bug fixes:


- Fix excluded items in navigation [ale-rt] (#2516)
- Add basic validators for the portal action controlpanel forms (#2689)
- Fix wrong msgids in link management control panel [erral] (#2788)
- Fix errors that abort the verification when debugging a DB with ./bin/instance verifydb -D.
  [pbauer] (#2792)
- Add summary of all errors when verifying a DB with ./bin/instance verifydb.
  [pbauer] (#2798)
- Fixed unstable SearchableText and Scenario Type querystring robot tests.  [maurits] (#2808)
- Fixed unstable Markup Control Panel and other robot tests.   [maurits] (#2809)


5.2rc1 (2019-03-04)
-------------------

New features:


- Views for title and description. [iham] (#2740)
- Display wsgi-state plus name and version of the server in the controlpanel
  [pbauer] (#2770)
- Enable dropdown-navigation for new sites by default. [pbauer] (#2772)


Bug fixes:


- Resolve circular dependency between `Products.CMFPlone` and `plone.i18n` by
  moving `ILanguageSchema` there. [sallner] (#2049)
- Use correct permission for mail controlpanel form so that Site Administrators
  can also edit. [fredvd] (#2688)
- Make linkintegrity robot test more reliable [MrTango] (#2752)
- Check only once if Products.ATContentTypes is available. [gforcada] (#2765)
- Fix redirection to `came_from` when url matches LOGIN_TEMPLATE_ID partly
  [petschki] (#2771)


5.2b1 (2019-02-13)
------------------

Breaking changes:


- Factor out all static resources and the ``plone-compile-resources`` script
  into plone.staticresources. [thet] (#2542)


New features:


- PLIP 1486: Merge Products.RedirectionTool into core. Allow users to manage
  redirects on their site and aliases to content. See
  https://github.com/plone/Products.CMFPlone/issues/1486 [staeff, maurits]
  (#1486)
- Added multilevel dropdown navigation [agitator] (#2516)
- No longer mark special links by default. [pbauer] (#2736)


Bug fixes:


- Switched allowedRolesAndUsers indexer from 'View' to the correct permission
  'Access contents information' for displaying metadata. 'View' permission
  should be used on the item itself. The change should not matter for default
  Plone workflows, since they always use those permissions together. [agitator]
  (#260)
- deprecate catalog_get_all(catalog) in favor of catalog.getAllBrains()
  [pbauer] (#2258)
- Restore the possibility to sort catalog query results with multiple indexes
  (#2464)
- Review list portlet showed nothing to review with plone.app.multilingual, As
  WorkflowTool bypassed languages only for p.a.m<2.x or linguaplone. fixed and
  now compatible to both lang-bypassing methods. [iham] (#2595)
- Fixed fallback to default view when selected layout does not exist for
  Folder. [gbastien] (#2645)
- The patched init method for the class zope.sendmail.mailer.SMTPMailer has
  been updated, fixing a bug that was preventing to send emails. [ale-rt,
  nazrulworld] (#2665)
- a11y: Added role attribute for portalMessage [nzambello] (#2675)
- Fix several warnings shown when running tests on Python 3+. [gforcada]
  (#2683)
- fixed Python 3 related str decoding issue in breadcrumbs (#2694)
- Fixed unstable robot test Scenario: A page is opened to edit in TinyMCE.
  [maurits] (#2707)


5.2a2 (2018-12-30)
------------------

New features:


- New robot tests for querystring in Collection type. Now almost all
  querystring types are robot tested. [llisa123] (#2489)
- Add ``load_async`` and ``load_defer`` attributes to resource registries
  bundle settings. When set, ``<script>`` tags are rendered with
  ``async="async"`` resp. ``defer="defer"`` attributes. You also need to empty
  the ``merge_with`` property of your bundle, because production bundles
  (``default.js`` and ``logged-in.js``) are never loaded with async or defer.
  The default.js includes jQuery and requirejs and those are needed at many
  places and therefore cannot be loaded asynchronously. Refs: #2649, #2657.
  [thet] (#2649)


Bug fixes:


- Delete ``fa_ir.js``. Keep ```fa_IR.js``. [maurits] (#2620)
- Forward port TinyMCE fixes from 5.1 [vangheem] (#2630)
- Fix robot test test_edit_user_schema: Fieldname was set duplicate (first by
  JS, then by robot). [jensens] (#2669)

5.2a1 (2018-11-08)
------------------

Breaking changes:

- Removed generateUniqueId.py skins script (after it was added to Products.Archetypes).
  This script is no longer available outside Archetypes world.
  #1801
  [jensens]

- Remove all dependencies on plone.app.controlpanel.
  Third party code need either to depend on plone.app.controlpanel 4.0,
  which is a backward compatibility package only, or also update to not depend on it anymore.
  [jensens]

- Removed check_id.py skin script.  Replaced with utils.check_id function.
  #1801 and #2582.
  [maurits]

- Removed my_worklist.py skin script. #1801
  [reinhardt]

- Removed getObjectsFromPathList.py skin script. #1801
  [reinhardt]

- Removed isExpired.py skin script. #1801
  [reinhardt]

- Removed redirectToReferrer.py skin script. #1801
  [tlotze]

- Removed enableHTTPCompression.py skin script. #1801
  [tlotze]

- Removed setAuthCookie.py skin script. #1801
  [tlotze]

- Stop configuring 'View History' permission which was removed from Zope.
  [davisagli]

- Removed legacy resource registries portal_css and portal_javascripts;
  no conditional handling.
  [ksuess]

New features:

- Factored out human_readable_size method for replacing getObjSize.py;
  removed getObjSize.py. #1801
  [reinhardt]

- Update TinyMCE to 4.7.13
  [erral]

- New browser view based login code - merged from plone.login (credits to esteele, pbauer, agitator, jensens, et al).
  `portal_skins/plone_login` is now gone, see PLIP #2092.
  Also, password reset view moved to login subfolder to keep things together.
  Some testbrowser based tests needed changes because of z3c.form based login form .
  The Plone specific, rarely used cross site __ac cookie SSO feature/hack was removed.
  In case somebody needs this, please make it an addon package.
  Better use a field proven, more secure way, like OAuth2, Shibboleth or something similar.
  [jensens, et al]

- Upgrade grunt + plugins to same versions as in
  mockup https://github.com/plone/mockup/pull/870
  [sunew]

- Upgrade less in bower.json to the same version as already used
  in the generated package.json in compile_resources.py.
  [sunew]

- Add utility-method safe_nativestring.
  [pbauer]

- Rename safe_unicode to safe_text and safe_encode to safe_bytes. Keep old aliases.
  [pbauer]
- Add a ``bin/instance verifydb`` command which can be used to check
  that all records in the database can be successfully loaded.
  This is intended to help with verifying a database conversion
  from Python 2 to Python 3.
  [davisagli]

Bug fixes:

- Modernize robot keywords that use "Get Element Attribute"
  [ale-rt]

- remove plone.app.folder dependency
  [petschki]

- move GopipIndex Class to plone.folder
  [petschki]

- Fixed getObjSize indexer for Python 3. #2526
  [reinhardt]
- Fix toolbar menu on mobile #2333.
- make groups_modify_roles test more robust.
  [tschorr]

-- Fix wrong CSS property to allow correct word-break.
  [tmassman]

 Fix toolbar menu on mobile #2333.
  [tmassman]

- Removed the ``raiseUnauthorized`` skin script.
  If you use this, please do permission checking in your own Python code instead (likely in a browser view).
  Refs `issue 1801 <https://github.com/plone/Products.CMFPlone/issues/1801>`_.
  [maurits]

- Remove the devdependencies from bower.json - they are just used for running tests in mockup, not here.
  [sunew]

- Adapt tests to `Products.GenericSetup >= 2.0` thus requiring at least that
  version.
  [icemac]

- Some tools from CMFCore are now utilities
  [pbauer]

- Fix failing thememapper robot test after rebuild of thememapper bundle in p.a.theming PR 148
  [sunew]

- Remove five.pt for Zope 4
  [jensens]

- Changes for Zope 4 compatibility in maintenance controlpanel.
  [thet]

- Render exceptions using an exception view instead of standard_error_message.
  [davisagli]

- Remove old PlacelessTranslationService.
  [jensens, ksuess]

- Fix controlpanel quickinstaller view:
  A not yet installed product must not return any upgrade info.
  [jensens]

- Fix to make plone/plone.session#11 work:
  Make test for installation of  plone.session more explicit.
  [jensens]

- Advanced Catalog Clear And Rebuild feature showed wrong processing time due to new queue processing.
  This was fixed bei calling ``processQueue()`` after indexing.
  [jensens]

- Some nested `section id="edit-bar"` tag in folder_contents page #2322
  [terapyon]

- Remove ``plone-generate-gruntfile`` (it is all available through ``plone-compile-resources``).
  [jensens]

- Migrate from ``slimit`` to ``calmjs.parse`` for the JavaScript cooker #2616
  [metatoaster]


New Features:

- Update to latest mockup
  [frapell]

- Provide an utility ``dump_json_to_text`` that works both on Python 2.7 an Python 3.
  [ale-rt]

- Prepare for Python 2 / 3 compatibility.
  [pbauer]

- Fix imports to work with Python 3.
  [pbauer]

- Mockup update.
  [thet]

- add link to Plone.org VPAT accessibility statement
  [tkimnguyen]

Bug Fixes:

- Remove last legacy Javascript ``highlight-searchterms.js``.
  Removes also the skins folder ``plone_ecmascript``.
  It was broken for all (Google, other search engines, own live search);
  JS worked only when coming from Plone detailed search.
  [jensens]

- Fix an undefined variable in a test helper function
  [ale-rt]

- Let the ``combine-bundles`` import step also work when the ``IBundleRegistry`` keyword is not in ``registry.xml``, but in a ``registry`` directory.
  `Issue 2520 <https://github.com/plone/Products.CMFPlone/issues/2502>`_.
  [maurits]

- Get rid of obsolete ``X-UA-Compatible`` header.
  [hvelarde]

- Fix registration of ``robots.txt`` browser view to avoid ``AttributeError`` on Zope's root (fixes `#2052 <https://github.com/plone/Products.CMFPlone/issues/2052>`_).
  [hvelarde]

- Get rid of obsolete ``X-UA-Compatible`` header.
  [hvelarde]

- Add test for issue #2469.
  [jensens]

- Fixed tests when IRichText behavior is used.
  IRichText -> IRichTextBehavior
  This is a follow up to `issue 476 <https://github.com/plone/plone.app.contenttypes/issues/476>`_.
  [iham]

- Remove unused mail_password.py from skins/plone_scripts
  [agitator]

- Hide ``plone.app.querystring`` from add-ons control panel.
  Fixes `issue 2426 <https://github.com/plone/Products.CMFPlone/issues/2426>`_.
  [maurits]

- Fix tests after changes in disallowed object ids in Zope.
  [pbauer]

- Do not include too new upgrades when upgrading Plone Site.
  Otherwise the Plone Site ends up at a newer version that the filesystem code supports,
  giving an error when upgrading, and resulting in possibly missed upgrades later.
  Fixes `issue 2377 <https://github.com/plone/Products.CMFPlone/issues/2377>`_.
  [maurits]

- After site creation, do not render the add-site template: we redirect anyway.
  [maurits]

- Unflakied a unit test.
  [Rotonen]

- Do not show TinyMCE menu items with no subitems, Fixes #2245.
  [mrsaicharan1]

- Fix Exception-View when main_template can't be rendered. Fixes #2325.
  [pbauer]

- Render exceptions as text, not html to fix format of infos after traceback.
  Display as <pre> for basic and normal error templates.
  [pbauer]

- Removed extra methods and tests for CMFQuickInstallerTool.
  Moved those to the Products.CMFQuickInstallerTool package.
  [maurits]

- Added tests for add-ons control panel.
  Add a link to the Site Setup.
  Let ``get_product_version`` work when you call it with ``CMFPlacefulWorkflow`` too.
  [maurits]

- Fix bad domain for translating password reset mails.
  [allusa]

- Ignore invalid ``sort_on`` parameters in catalog ``searchResults``.
  Otherwise you get a ``CatalogError``.
  I get crazy sort_ons like '194' or 'null'.
  [maurits]

- Register the ``ExceptionView`` for the unspecific ``zope.interface.Interface`` for easier overloading.
  Fixes a problem, where plone.rest couldn't overload the ExceptionView with an adapter bound to ``plone.rest.interfaces.IAPIRequest``.
  [thet]

- Fixed linkintegrity robot tests.  [maurits]

- Fixed flaky actions controlpanel tests by waiting longer.  [maurits]

- Require AccessControl 4.0b1 so ``guarded_getitem`` is used.
  Part of PloneHotfix20171128.  [maurits]

- Improved isURLInPortal according to PloneHotfix20171128.
  Accept only http/https, and doubly check escaped urls.  [maurits]

- Fix exception view when called on Zope-root. Fixes #2203.
  [pbauer]

- added CSS hyphenation support for toolbar for avoiding ugly text wrapping
  Fixes `issue 723 <https://github.com/plone/Products.CMFPlone/issues/723>`_.
  [ajung]

- Increase compatibility with Python3.
  [ale-rt]

- Show example for expression in actions control panel.
  [maurits]

- Fix test where you cannot instantiate a PythonScript with the id script.
  [pbauer]

- Set the status of an exception view according to the exception type.
  Fixes `issue 2187 <https://github.com/plone/Products.CMFPlone/issues/2187>`_.
  [maurits]

- Use absolute imports for Python3 compatibility
  [ale-rt]

- Fallback for missing date in DefaultDublinCoreImpl no longer relies on
  bobobase_modification_time.
  [pbauer]

- Display real version of Zope, not of the empty meta-package Zope2.
  [pbauer]

- Add zcml-condition plone-52 for conditional configuration.
  [pbauer]

- Use getSite in set_own_login_name to get the portals acl_users.
  [pbauer]

- Fix test issue with rarely used multi-site SSO feature.
  ``came_from`` on ``@register`` link would point to wrong site.
  Completely removed ``came_from`` on ``@@register`` link.
  It does not make much sense anyway and we test nowhere if there is a came_from on that link.
  [jensens]

- Remove deprecated ``type`` attribute from ``script`` and ``link`` tags.
  [newbazz]

- Render tinymce attributes correctly in Python3.
  [sallner]

- Remove unresolved dependencies of plone-final to cssregistry and jsregistry.
  [pbauer]


5.1rc2 (unreleased)
-------------------

New features:

- Toolbar: Allow configuration of the toolbar and submenu width via pattern variables.
  [thet]

- Update npm dependencies.
  [thet]

Bug fixes:

- Fixed add-on listed as uninstalled when the default profile is not the first alphabetically.
  Fixes `issue 2166 <https://github.com/plone/Products.CMFPlone/issues/2166>`_.
  [maurits]

- Less variables: Fix calculation of screen max sizes.
  Max sizes were two pixels too high.
  [thet]

- Mockup update.
  [thet]

- Remove site path from path in show_inactive in catalog search
  [Gagaro]

- Don't raise Unauthorized on show_inactive check in catalog search
  [tomgross]

- Bump metadata.xml version.
  [thet]

- Extract CMFDefault specific config from `meta.zcml` into `meta-bbb.zcml`
  to allow AT free and AT included sites.
  [tomgross]

- Add basic tests for all main zmi management screens.
  [pbauer]

- Fixes #2105: how to get ``email_from_name`` information in sendto_form.
  [cekk]

5.1rc1 (2017-09-10)
-------------------

Breaking changes:

- Replaced cssmin with PyScss to ensure Python 3 compatibility and maintainability.
  Removed dependency to cssmin, so could break dependency for third party addons that depend on it.
  Introduced PyScss as a drop in replacement that could also do more things.
  Discussion on that at https://github.com/plone/Products.CMFPlone/issues/1800
  [loechel]

- Fix and migrate safe_html filter completely into Plone registry and sync settings with TinyMCE.
  Also some unused options in controlpanel where removed, like stripped_combinations and class_blacklist.
  [MrTango]

New features:

- Update ``plone-legacy-compiled.js`` and ``plone-legacy-compiled.css``.
  [thet]

- Update mockup to latest version.
  [thet]

- Added ``Show Toolbar`` permission.
  [agitator]

- Add RobotFramework screenshot tests for the Plone documentation.
  [datakurre, polyester]

- Add jqtree-contextmenu to the resource registry
  [b4oshany]

- Add js-shortcuts to the resource registry
  [b4oshany]

Bug fixes:

- Recover missing dashboard (user actions)
  https://github.com/plone/Products.CMFPlone/issues/1132
  [fgrcon]

- Remove the right padding on toolbar submenu entries.
  That looked a bit weird.
  [thet]

- Fixed accidentally removing permissions when saving the ``portal_controlpanel`` settings in the ZMI.
  Fixes `issue 1376 <https://github.com/plone/Products.CMFPlone/issues/1376>`_.  [maurits]

- Do not open links on a new tab as this is against basic usability guidelines.
  [hvelarde]

- add :focus class on toolbar for keyboard users  (https://github.com/plone/Products.CMFPlone/issues/1620)
  [polyester]

- Fix empty DX add_forms if formlib is also installed thru addon dependencies
  [MrTango]

- Update TinyMCE links (tinymce-controlpanel) to https
  [svx]

- Fix ``utils.get_top_site_from_url`` to work with non-OFS contexts.
  [thet]

- remove mention of "retina" (https://github.com/plone/Products.CMFPlone/issues/2123)
  [tkimnguyen]


5.1b4 (2017-07-03)
------------------

New features:

- Integrate ``mockup-patterns-structureupdater`` for updating title and description depending on the current context on the folder contents page.
  [thet]

- Updated jqtree to 1.4.1 from 1.3.3
  [b4oshany]

- Update mockup to latest version.
  [thet]

- add registry settings for thumb and icon handling  in tables, lists and portlets
  https://github.com/plone/Products.CMFPlone/issues/1734 (PLIP)
  recompiled bundle plone-logged-in
  requires upgrade step (reapply profile)
  [fgrcon]

- Update mockup to latest version.
  [thet]

- new metadata catalog column mime_type
  https://github.com/plone/Products.CMFPlone/issues/1995
  [fgrcon]

- Include TinyMCE 4.5.6
  [frapell]

Bug fixes:

- Use explicit @@footer view for footer portlet.
  [agitator]

- Translate image scales in patterns.
  [Gagaro]

- Gruntfile generation no longer fails on introspecting resourceDirectory
  configurations using a plone.browserlayer layer, by loading all layers
  configured for the site used during generation.
  Fixes `issue 2080 <https://github.com/plone/Products.CMFPlone/issues/2080>`_.
  [seanupton]

- fixed css-classes for thumb scales ...
  https://github.com/plone/Products.CMFPlone/issues/2077
  [fgrcon]

- Fix current value in group details edit form.
  [Gagaro]

- Fixed KeyError ``productname`` when there is a broken add-on in the add-ons control panel.
  Fixes `issue 2065 <https://github.com/plone/Products.CMFPlone/issues/2065>`_.
  [maurits]

- Fix ``test_tinymce.robot`` test to work with latest related items changes.
  [thet]

- Fix expiration date when displaying in registered form.
  [allusa]

- Remove TinyMCE pattern options from the body, as these are always set on the richtext fields mimetype selector or - if not there - on the textfield itself.
  Refs: https://github.com/plone/Products.CMFPlone/pull/2059
  [thet]

- Let TinyMCE options for the related items widget be generated by ``plone.app.widgets.utils.get_relateditems_options``.
  This aligns the options to how the related items widget is used elsewhere.
  Fixes https://github.com/plone/Products.CMFPlone/issues/1974
  [thet]

- CMFCore ``WarningInterceptor`` test base class was gone and is not needed in Plone, so removed.
  [jensens]

- Fix default value for ``robots.txt`` to avoid issues with content containing "search" in the id.
  [hvelarde]

- Remove references to Products.CMFDefault on meta.zcml
  [gforcada]

- Adapt tests to render social metadata only if you are anonymous.
  [bsuttor]

- Fix search term munging with queries that include and, or and not.
  [malthe]

- Fix issue where catalog search with path failed when path had inaccessible
  (private) levels
  [datakurre]

- Add constraint to avoid filling ``twitter_username`` field with strings starting with a "@" character.
  [hvelarde]

- Fixed addons/donations links, removed dead "add your site" link
  [sgrepos]

- Fix issue where collapsed toolbar was not initialized properly on page
  refresh, resulting wide blank space between collapsed toolbar and page
  content
  [datakurre]

- Removed "change portal events" permission
  [kakshay21]

- Updated dead link to the error reference docs
  [sgrepos]

- Do not rely on order in test of generated body classes ``browser.txt``.
  [jensens]

- Fix possible ``mechanize.AmbiguityError`` in controlpanel tests.
  [jensens]

5.1b3 (2017-04-03)
------------------

New features:

- Adapt code and tests to the new indexing operations queueing.
  Part of PLIP 1343: https://github.com/plone/Products.CMFPlone/issues/1343
  [gforcada]

- Make use of plone.namedfile's tag() function to generate img tags. Part of plip 1483.
  [didrix]

- Add retina scales settings in image handling. Part of plip 1483
  [didrix]

Bug fixes:

- Use canonical url instead of absolute url for RSS feed items.
  This code is used for the social viewlet too.
  So default pages are reported with their parent url.
  Fixes `layout issue 118 <https://github.com/plone/plone.app.layout/issues/118>`_.
  [maurits]

- Fix social media schema field types of ``twitter_username``, ``facebook_app_id`` and ``facebook_username`` to be ``ASCIILine`` instead of ``TextLine``.
  [hvelarde]

- Show version of products in Add-ons control panel configlet.
  This fixes https://github.com/plone/Products.CMFPlone/issues/1472.
  [hvelarde]

- Resource registry legacy bundle cooking: Exit early with a warning, if preconditions to build are not given (no compilation paths).
  Allow cooking CSS, even if no JS is defined.
  Log all important steps of the cooking process.
  [thet]

- Remove unused ``plone.css`` from static repository.
  [thet]

- Check for ``AccessInactivePortalContent`` for each path in a catalog query.
  This solves a problem, where Editors couldn't see inactive content, even though they had the required permission on a subpath of the portal (e.g. a subsite).
  [thet]

- Test: Wrong use of assertTrue in testResourceRegistries.
  [jensens]

- Fix issue popped iup after fix of use of assertTrue in testResourceRegistries: insert-before in legacy resource import was broken.
  [jensens]


5.1b2 (2017-02-20)
------------------

Bug fixes:

- Fix packaging error.
  [esteele]

5.1b1 (2017-02-20)
------------------

Breaking changes:

- Add helper method to get all catalog entries from a given catalog: ``Products.CMFPlone.CatalogTool.catalog_get_all``.
  In Products.ZCatalog before 4.0 a catalog call without a query returned all catalog brains.
  This can be used as a replacement where it is needed, for example in tests.
  [thet, gogobd]

- Remove ``query_request`` from CatalogTool's search method, as it isn't supported in Products.ZCatalog 4 anymore.
  [thet]

- Removed our patch that added ``secureSend`` to the ``MailHost``.
  This was originally scheduled for removal in Plone 5.0.  See `issue
  965 <https://github.com/plone/Products.CMFPlone/issues/965>`_.
  [maurits]

- The related items widget has changed a lot.
  See the Mockup changelog for 2.4.0 here: https://github.com/plone/mockup/blob/master/CHANGES.rst

- All css classes named ``enableUnloadProtection`` were changed to ``pat-formunloadalert`` to trigger that pattern.
  Templates using ``enableUnloadProtection`` should change to ``pat-formunloadalert`` too.
  This change shouldn't impact too much, because the form unload protection didn't work at all in Plone 5 until now.
  [thet]

- MimetypesRegistry icons are now a browser resource directory instead of skins folder.
  [jensens]

- Remove unused ``plone_scripts`` (not used nor tested anywhere in coredev) [jensens, davisagli]

    - ``add_ext_editor.py``
    - ``author_find_content.py``
    - ``canSelectDefaultPage.py`` with tests
    - ``create_query_string.py``
    - ``createMultiColumnList.py``
    - ``displayContentsTab.py``
    - ``formatColumns.py`` with tests
    - ``getAllowedTypes.py``
    - ``getGlobalPortalRoles.py``
    - ``getNotAddableTypes.py``
    - ``getPopupScript.py``
    - ``getPortalTypeList.py`` and metadata
    - ``getPortalTypes.py``
    - ``getSelectableViews.py`` with tests
    - ``hasIndexHtml.py`` with tests
    - ``navigationParent.py`` with test
    - ``plone_log.py``
    - ``plone.css.py``
    - ``returnNone.py`` with occurrence refactored
    - ``reverseList.py`` with test
    - ``sort_modified_ascending.py``

- Move scripts ``datecomponents.py`` and ``show_id.py`` to Archetypes
  [jensens, davisagli]

- Remove methods of the ``@@plone`` view that were marked for deprecation:
  - ``showEditableBorder`` (use ``@@plone/showToolbar``)
  - ``mark_view`` (use ``@@plone_layout/mark_view``)
  - ``hide_columns`` (use ``@@plone_layout/hide_columns``)
  - ``icons_visible`` (use ``@@plone_layout/icons_visible``)
  - ``getIcon`` (use ``@@plone_layout/getIcon``)
  - ``have_portlets`` (use ``@@plone_layout/have_portlets``)
  - ``bodyClass`` (use ``@@plone_layout/bodyClass``)
  [davisagli]

- Move plone_content skin templates into Products.ATContentTypes as browser views.
  [gforcada]

New features:

- Added ``ok`` view.  This is useful for automated checks, for example
  httpok, to see if the site is still available.  It returns the text
  ``OK`` and sets headers to avoid caching.
  [maurits]

- Make contact form extensible. This fixes https://github.com/plone/Products.CMFPlone/issues/1879.
  [timo]

- Don't minify CSS or JavaScript resources if they end with ``.min.css`` resp. ``.min.js``.
  [thet]

- Add ``safe_encode`` utility function to ``utils`` to safely encode unicode to a specified encoding.
  The encoding defaults to ``utf-8``.
  [thet]

- The password reset templates were changed to make use of ``content-core`` macros.
  [thet]

- Add utility method to retrieve the top most parent request from a sub request.
  [thet]

- Add ``mockup-patterns-relateditems-upload`` resource, which can be used in custom bundles to add the upload feature in the related items widget.
  [thet]

- Move ``get_top_site_from_url`` from plone.app.content to ``utils.py`` and make it robust against unicode paths.
  This function allows in virtual hosting environments to acquire the top most visible portal object to operate on.
  It is used for example to calculate the correct virtual root objects for Mockup's related items and structure pattern.
  [thet]

- Add sort_on field to search controlpanel.
  [rodfersou]

- PLIP 1340: Deprecate portal_quickinstaller.
  You should no longer use CMFQuickInstallerTool methods, but GenericSetup profiles.
  See https://github.com/plone/Products.CMFPlone/issues/1340
  [maurits]

- Include mockup 2.4.0.
  [thet]

- PasswordResetTool moved from its own package to here (includes cleanup and removal of ``getStats``).
  [tomgross]

- Prevent workflow menu overflowing in toolbar [MatthewWilkes]

- Add default icon for top-level contentview and contentmenu toolbar entries [alecm]

- Toolbar: Make menu hover background fit whole menu width. [thet]

- Toolbar: Don't force scroll buttons to be left, when toolbar is right. [thet]

- Toolbar: Make first level list items expand the whole toolbar width - also when scroll buttons are shown. [thet]

- Toolbar: Make scroll buttons expand whole toolbar width. [thet]

- Toolbar: Let the toolbar submenus be as wide as they need to be and do not break entries into multiple lines. [thet]

- Resource Registry:
  In ``debug-mode`` (zope.conf, buildout) do not load cache the production bundle.
  [jensens]

- Resource Registry:
  In ``debug-mode`` (zope.conf, buildout) do not ignore development mode for anonymous users.
  [jensens]

- Resource Registry: If file system version is newer than ``last_compilation`` date of a bundle, use this as ``last_compilation`` date.
  [jensens]

- Simplify generated Gruntfile.js (DRY)
  [jensens]

- Fix: Do not modify the Content-Type header on bundle combine.
  [jensens]


Bug fixes:


- Moved getToolByName early patch to the later patches.
  This fixes a circular import.
  See `issue #1950 <https://github.com/plone/Products.CMFPlone/issues/1950>`_.
  [maurits]

- Include JS Patterns when loading a page via ajax or an iframe [displacedaussie]

- Restore ability to include head when loading via ajax [displacedaussie]

- Added security checks for ``str.format``.  Part of PloneHotfix20170117.  [maurits]

- Fixed workflow tests for new ``comment_one_state_workflow``.  [maurits]

- Fixed sometimes failing search order tests.  [maurits]

- Load some Products.CMFPlone.patches earlier, instead of in our initialize method.
  This is part of PloneHotfix20161129.
  [maurits]

- Depend on CMFFormController directly, because our whole login process is based on it and its installed in the GenericSetup profile.
  Before it was installed indeirectly due to a dependency in some other package which is gone.
  [jensens]

- Fix Search RSS link condition to use search_rss_enabled option and use
  rss.png instead of rss.gif that doesn't exist anymore.
  [vincentfretin]

- Fix potential KeyError: admin in doSearch in Users/Groups controlpanel.
  [vincentfretin]

- Let the ``mail_password_template`` and ``passwordreset`` views retrieve the expiry timeout from the view, in hours.
  [thet]

- Fix i18n of the explainPWResetTool.pt template.
  [vincentfretin]

- Remove "Minimum 5 characters" in help_new_password in pwreset_form.pt like
  in other templates.
  [vincentfretin]

- Fix duplicate i18n attribute 'attributes' in controlpanel/browser/actions.pt
  [vincentfretin]

- Use "site administration" in lower case in accessibility-info.pt and
  default_error_message.pt like in other templates.
  [vincentfretin]

- Support adding or removing bundles and resources on a request when working with resource tiles in a subrequest.
  [thet]

- Remove jquery.cookie from plone-logged-in bundle's stub_js_modules.
  The toolbar, which has a dependency on jquery.cookie,
  was moved from the plone bundle to plone-logged-in in CMPlone 5.1a2.
  [thet]

- Fix various layout issues in toolbar [alecm]

- Style display menu headings differently from actions [alecm]

- Avoid dependency on plone.app.imaging. [davisagli]

- Fix TinyMCE table styles [vangheem]

- Fix TinyMCE content CSS support to allow themes to define
  external content CSS URLs (as with CDN like setup).
  [datakurre]


- Add utf8 headers to all Python source files. [jensens]

- Add default icon for top-level contentview and contentmenu toolbar entries [alecm]
- Reset and re-enable ``define`` and ``require`` for the ``plone-legacy`` bundle in development mode.
  Fixes issues with legacy scripts having RequireJS integration in development mode.
  In Production mode, resetting  and re-enabling is done in the compiled bundle.
  [thet]

- Apply security hotfix 20160830 for ``z3c.form`` widgets.  [maurits]

- Fixed tests in combination with newer CMFFormController which has the hotfix.  [maurits]

- Apply security hotfix 20160830 for ``@@plone-root-login``.  [maurits]

- Apply security hotfix 20160830 for ``isURLInPortal``.  [maurits]

- Enable unload protection by using pattern class ``pat-formunloadalert`` instead ``enableUnloadProtection``.
  [thet]

- Provide the image scale settings in TinyMCE image dialog.
  [thet]

- Fix link on ``@@plone-upgrade``
  [gforcada]

- Remove LanguageTool layer.
  [gforcada]

- Use fork of grunt-sed which is compatible with newer grunt version.
  [gforcada]

- Move some tests from ZopeTestCase to plone.app.testing.
  [gforcada, ivanteoh, maurits]

- wording changes for social media settings panel
  [tkimnguyen]

- URL change for bug tracker, wording tweaks to UPGRADE.txt
  [tkimnguyen]

- Cleanup code of resource registry.
  [jensens]

- Fix plone-compile-resources:
  Toolbar variable override only possible if prior defined.
  Define ``barcelonetaPath`` if ``plonetheme.barceloneta`` is available (but not necessarily installed).
  [jensens]

- Include inactive content in worklists.  [sebasgo]

- Fix #1846 plone-compile-resources: Missing Support for Sites in Mountpoints
  [jensens]

- Do not use unittest2 (superfluous since part of Python 2.7).
  [jensens]

- Fix security test assertion:
  TestAttackVectorsFunctional test_widget_traversal_2 assumed a 302 http return code when accessing some private API.
  Meanwhile it changed to return a 404 on the URL.
  Reflect this in the test and expect a 404.
  [jensens]

- Fix atom.xml feed not paying attention for setting to show about information
  [vangheem]

- Fix imports from package Globals (removed in Zope4).
  [pbauer]

- Skip one test for zope4.
  [pbauer]

- Fix csrf-test where @@authenticator was called in the browser.
  [pbauer]

- Do not attempt to wrap types-controlpanel based on AutoExtensibleForm and
  EditForm in Acquisition using __of__ since
  Products.Five.browser.metaconfigure.simple no longer has
  Products.Five.bbb.AcquisitionBBB as a parent-class and thus no __of__.
  Anyway __of__ in AcquisitionBBB always only returned self since
  Products.Five.browser.metaconfigure.xxx-classes are always aq-wrapped
  using location and __parent__. As a alternative you could use
  plone.app.registry.browser.controlpanel.ControlPanelFormWrapper as
  base-class for a controlpanel since ControlPanelFormWrapper subclasses
  Products.Five.BrowserView which again has AcquisitionBBB.
  [pbauer]

- Remove eNotSupported (not available in Zope 4)
  [tschorr]

- Remove deprecated __of__ calls on BrowserViews
  [MrTango]

- Test fix (Zope 4 related): More General test if controlpanel back link URL is ok.
  [jensens]


5.1a2 (2016-08-19)
------------------

Breaking changes:

- Move toolbar resources to plone-logged-in bundle and recompile bundles.
  [davilima6]

- Don't fail, if ``timestamp.txt`` was deleted from the resource registries production folder.
  [thet]

- Add ``review_state`` to ``CatalogNavigationTabs.topLevelTabs`` results.
  This allows for exposing the items workflow state in portal navigation tabs.
  [thet]

- Remove discontinued module ``grunt-debug-task`` from ``plone-compile-resources``.
  [jensens]

- Remove deprecated resource registrations for ``mockup-parser`` and ``mockup-registry`` from mockup-core.
  Use those from patternslib instead.
  [thet]

- ``plone-compile-resources``: Install ``grunt-cli`` instead of depending on an installed ``grunt`` executable.
  If you already have a auto-generated ``package.json`` file in buildout directory, remove it.
  [thet]


- Moved code around and deprecated old locations in ``Products/CMFPlone/patterns/__init__``.
  This goes together with same pattern settings changes in ``plone.app.layout.globals.pattern_settings``.
  Also moved general usable ``./patterns/utils/get_portal`` to ``./utils/.get_portal``.
  Deprecated ``./patterns/utils/get_portal`` and ``./patterns/utils/get_portal``.
  [jensens]


New features:

- Updated components directory, recompiled bundles.
  [thet]

- Align bower components with newest mockup + documentation updates on mockup update process.
  [thet]

- Ignore a bit more in ``.gitignores`` for CMPlones bower components.
  [thet]

- Added setting to editing controlpanel to enable limit of keywords to the current navigation root.
  [jensens]

- Make login modal dialog follow any redirects set while processing the login request.
  [fulv]

- Add link to training.plone.org
  [svx]

- Allow to define multiple ``tinymce-content-css`` in theme ``manifest.cfg`` files, separated by a comma.
  [thet]

- Update npm package dependencies.
  [thet]

- Supported ``remove`` keyword for configlets in controlpanel.xml.  [maurits]

- Deprecated Gruntfile generation script ``plone-generate-gruntfile``.
  Modified the ``plone-compile-resources`` script to support more parameters in order to take over that single task too.
  Also clean up of parameters, better help and refactored parts of the code.
  [jensens]

- Make filter control panel work with new version of safe HTML transform
  [tomgross]
- Allow to hide/show actions directly from the Actions control panel list
  [ebrehault]


Bug fixes:

- Have more patience in the thememapper robot test.
  [maurits]

- Upgrade ``less-plugin-inline-urls`` to ``1.2.0`` to properly handle VML url node values in CSS.
  [thet]
- Fixed adding same resource/bundle to the request multiple times.
  [vangheem]

- Fixed missing keyword in robot tests due to wrong documentation lines.
  [maurits]

- TinyMCE default table styles were broken after install due to a wrong default value.
  [jensens]

- Rewording of some Site control panel text [tkimnguyen]

- Fixed syntaxerror for duplicate tag in robot tests.  [maurits]

- Marked two robot tests as unstable, non-critical.
  Refs https://github.com/plone/Products.CMFPlone/issues/1656  [maurits]

- Use ``Plone Test Setup`` and ``Plone Test Teardown`` from ``plone.app.robotframework`` master.  [maurits]

- Let npm install work on windows for plone-compile-resources.
  [jensens]

- Don't fail, when combining bundles and the target resource files (``BUNLDE-compiled.[min.js|css]``) do not yet exist on the filesystem.
  Fixes GenericSetup failing silently on import with when a to-be-compiled bundle which exists only as registry entry is processed in the ``combine-bundle`` step.
  [thet]

- Workaround a test problem with outdated Firefox 34 used at jenkins.plone.org.
  This Workaround can be removed once https://github.com/plone/jenkins.plone.org/issues/179 was solved.
  [jensens]

- Fix select2 related robot test failures and give the test_tinymce.robot scenario a more unique name.
  [thet]

- Add missing ``jquery.browser`` dependency which is needed by patternslib.
  [thet]

- Toolbar fixes:
  - Autoformat with cssbrush and js-beautify,
  - Remove ``git diff`` in line 105, which broke compilation.
  - Use patternslib ``pat-base`` instead of ``mockup-patterns-base``.
  - Remove dependency on deprecated ``mockup-core``.
  [thet]

- Removed docstrings from PropertyManager methods to avoid publishing them.  [maurits]

- Added publishing patch from Products.PloneHotfix20160419.
  This avoids publishing some methods inherited from Zope or CMF.  [maurits]

Fixes:

- Remove whitespaces in ``Products/CMFPlone/browser/templates/plone-frontpage.pt``.
  [svx]

- Fixed versioning for File and Image.
   [iham]

- Do not hide document byline viewlet by default;
  it is controlled by the `Allow anyone to view 'about' information` option in the `Security Settings` of `Site Setup` (closes `#1556`_).
  [hvelarde]

- Removed docstrings from some methods to avoid publishing them.  From
  Products.PloneHotfix20160419.  [maurits]

- Fix issue where incorrectly configured formats would cause TinyMCE to error
  [vangheem]

- Closes #1513 'Wrong portal_url used for TinyMCE in multilingual site',
  also refactors the patterns settings and cleans it up.
  [jensens]

- Removed inconsistency in the display of `Site Setup` links under 'Users and Groups'
  control panel.
  [kkhan]

- Only encode JS body if unicode in gruntfile generation script to avoid
  unicode error.
  [jensens]

- Only encode CSS body if unicode in gruntfile generation script to avoid
  unicode error.
  [rnix]

- Gruntfile failed if only css or only javascripts were registered.
  [jensens]

- Bundle aggregation must use ++plone++static overridden versions if any.
  [ebrehault]

- Fix bundle aggregation when bundle has no CSS (or no JS)
  [ebrehault]

- Fix relative url in CSS in bundle aggregation
  [ebrehault]

- Do not hard-code baseUrl in bundle to avoid bad URL when switching domains.
  [ebrehault]

- fix typo and comma splice error in HTML filtering control panel [tkimnguyen]

- Use zope.interface decorator.
  [gforcada]

- Remove advanced_search input which is in double.
  [Gagaro]


5.1a1 (2016-03-31)
------------------

Incompatibilities:

- Changed these ``section`` elements to ``div`` elements: ``#viewlet-above-content``, ``#viewlet-above-content-body``, ``#content-core``, ``#viewlet-below-content-body``.
  And these portlets ``section`` elements to ``aside`` elements: ``#portal-colophon``, ``#portal-footer-signature``.
  This might affect your custom styling or javascript.
  [maurits]

New:

- Upgrade to tinymce to 4.3.4
  [vangheem]

- For the controlpanel portlets, use the nearest site url as a base for the overview-controlpanel.
  This gives more flexibility for sub site controlpanels.
  [thet]

- added invisible-grid table styles
  [agitator]

- Control panel to manage portal actions
  [ebrehault]

- new less variable to configure the width of the toolbars submenu called ``plone-toolbar-submenu-width``.
  [jensens]

- new zcml feature "plone-51" added. Profile version set to 5101.
  Version references set to 5.1.0.
  [jensens]

- Registered post_handler instead of plone-final.  The plone-final
  import step now does nothing.  Instead, we redefined the old handler
  as a post_handler explicitly for our main profile.  This is
  guaranteed to really run after all other import steps, which was
  never possible in the old way.  The plone-final step is kept for
  backwards compatibility.
  [maurits]

- Remove Zope mention in logout form
  [tkimnguyen]

- Do not encode reply-to email address for contact-info form
  [tkimnguyen]

Fixes:

- Fixed displaying the body text of a feed item.  This is when
  ``render_body`` is switched on in the Syndication settings.
  [maurits]

- Make Gruntfile.js generation script a bit more verbose to show the effective
  locations of the generated bundles. This helps in case of non-working setups
  also as if bundle compilation was started in browser at a first run a and
  next run was run using the script and files were generated at different
  places than expected.
  [jensens]

- Ensured front-page is English when creating an English site.
  Previously, when creating an English site with a browser that
  prefers a different language, the body text ended up being in the
  browser language.  For languages without a front-page text
  translation the same happened: they got the other language instead
  of English.  [maurits]

- Fixed test error in ``test_controlpanel_site.py`` failed with random error.
  [jensens]

- Do not break background images relative urls in CSS when concatenating bundles
  [ebrehault]

- Fixed html validation: element nav does not need a role attribute.
  [maurits]

- Fixed html validation: section lacks heading.
  [maurits]


5.0.3 (2016-03-??)
------------------

Fixes:

- In the ``combine-bundles`` import step, make sure the Content Type
  header is not set to ``application/javascript``.  This would result
  in the ``plone-upgrade`` result page being shown in plain text.
  Fixes https://github.com/plone/Products.CMFPlone/issues/1436
  [maurits]


5.0.3c1 (2016-03-02)
--------------------

New:

- If a bundle does not provide any resources, do not attempt to compile it
  [vangheem]

- Build resource registry JavaScript for fix in not being able to develop js/css
  [vangheem]

- Include pat-moment for public javascript
  [vangheem]

- Add custom navigation root in TinyMCE configuration.
  [alecm]

- Add barceloneta theme path in less configuration.
  [Gagaro]

- Merge JS and CSS bundles into meta-bundles to reduce the number of requests
  when loading a page (PLIP #1277)
  [ebrehault]

Fixes:

- Toolbar cleanup: more less and less css, typo corrected in less variable,
  better readability with a darker background in submenu, use font fallback
  chain as in barcelonetta (works also w/o the theme).
  [jensens]

- Fix browser spell checking not working with TinyMCE
  [vangheem]

- Do not fail when viewing any page, or during migration, when Diazo
  is not installed and the persistent resource directory is not
  registered.  Fixes
  https://github.com/plone/Products.CMFPlone/issues/1187
  [maurits]

- Move hero on welcome page from theme into managed content.
  Issue https://github.com/plone/Products.CMFPlone/issues/974
  [gyst]

- Get ``email_from_name`` from the mail settings registry.
  Fixes https://github.com/plone/Products.CMFPlone/issues/1382
  [tmog]

- No longer rely on deprecated ``bobobase_modification_time`` from
  ``Persistence.Persistent``.
  [thet]

- Move p.a.discussion monkey patch for reindexing conversations to
  CatalogTool.py as p.a.discussion is part of Plone core.
  Issue https://github.com/plone/Products.CMFPlone/issues/1332
  [fredvd, staeff]

- Fix custom tinymce content styles not getting included correctly
  [vangheem]

- Fix timing problem with robot framework tests.
  [jensens]

- Upgrade TinyMCE to 4.3
  [vangheem]

- Fix use of icons in search results
  [vangheem]

- Mock MailHost on testing.py so that tests relying on mails can use it.
  [gforcada]

- Fix `aria-hidden` attribute control problem on toolbar
  https://github.com/plone/Products.CMFPlone/issues/866
  [terapyon]

- Sort relateditems tree by sortable_title in tinymce.
  [Gagaro]

- Return a JSON error instead of a the Plone error page when the requested
  resource is not text/html (fix #637).
  [ebrehault]


5.0.2 (2016-01-08)
------------------

Fixes:

- Fix url generation for tinymce when using virtual hosting. This fixing
  images not rendering properly in tinymce.
  [vangheem]

- build resources with latest mockup that provides better path criteria
  widget for the querystring pattern
  [vangheem]

- Fixed Forbidden error when using the users and groups overview as
  Site Administrator.  This could happen when there are users that
  inherit the Manager role from the Administrators group.
  Fixes issue https://github.com/plone/Products.CMFPlone/issues/1293
  [maurits]

- Fixed Unauthorized error in folder_full_view for anonymous users.
  Fixes issue https://github.com/plone/Products.CMFPlone/issues/1292
  [maurits]


5.0.1 (2015-12-17)
------------------

New:

- Add option to show/hide thumbs in site-controlpanel
  https://github.com/plone/Products.CMFPlone/issues/1241
  [fgrcon]

- Add icon fallback for addons in Site Setup (fixes `#1232`_)
  [davilima6]

- Explicitly provide id on search form and not depend on diazo magic
  adding the id in.
  [vangheem]

- Be able to stub JavaScript modules to prevent including the same
  javascript twice.
  [vangheem]

- Set Reply-to address in contact-info emails so you can reply to them.
  [tkimnguyen, maurits, davisagli]

- Added syndication for plone.app.contenttypes collections.
  [do3cc]

- Compress generated bundle CSS file when running ``plone-compile-resource``.
  [petschki]

- Added new commandline argument to plone-compile-resource: ``--compile-dir``.
  [petschki]

- Upgraded to patternslib 2.0.11.
  [vangheem]

- Allowed all TinyMCE settings to be set from control panel.
  [Gagaro]

- Added missing_value parameter to controlpanel list and tuple fields.
  [tomgross]

- Split hard coded JavaScript resources into separate method for easier
  customization.
  [tomgross]

Fixes:

- Fix internal links and images src to not include the domain.
  [Gagaro]

- Update Site Setup link in all control panels (fixes `#1255`_)
  [davilima6]

- In tests, use ``selection.any`` in querystrings.  And expect this in
  the default news and events collections.
  Issue https://github.com/plone/Products.CMFPlone/issues/1040
  [maurits]

- Add authenticator token to group portlet links
  [vangheem]

- Fix bbb global status message template rendering escaped html
  [vangheem]

- Avoid AttributeError if registry is not yet there for the
  JSRegistryNodeAdapter while migrating from older versions
  https://github.com/plone/Products.CMFPlone/pull/1246
  [frapell]

- remove deprecated icons ...
  https://github.com/plone/Products.CMFPlone/issues/1226
  [fgrcon]

- Also remove deprecated icons for archetypes
  [Gagaro]

- Fixed white space pep8 warnings.
  [maurits]

- Prevented breaking Plone when TinyMCE JSON settings fields contain
  invalid JSON.
  [petschki]

- Fixed #1199: prevent throwing error with mis-configured bundle.
  [vangheem]

- Fixed wrong sentence in front page.  There is no "Site Setup entry
  in the menu in the top right corner".  Replaced it by "Site Setup
  entry in the user menu".
  [vincentfretin]

- Fixed some i18n issues.
  [vincentfretin]

- Used unique traverser for stable resources to set proper cache headers.
  [alecm]

- Fixed "contains object" tinymce setting not getting passed into pattern
  correctly.  Fixes #1023.
  [vangheem]

- Fixed issue when csscompilation and/or jscompilation are missing in
  bundle registry record.
  [peschki]

- Fixed #1131: Allow to compile bundle with more than one resource.
  [timitos]

- Fixed issue where clicking tabs would cause odd scroll movement.
  [vangheem]

- When migration fails, do not upgrade addons or recatalog or update
  roles.
  [maurits]

- Default values for interfaces.controlpanel.IImagingSchema.allowed_sizes
  should be unicode.
  [kuetrzi]

- Don't depend on and install plone.app.widgets. plone.app.z3cform does it for
  us.
  [thet]


5.0 (2015-09-27)
----------------

- Update hero text. Remove "rocks" line, more descriptive link button.
  [esteele]

- Be able to provide table styles in tinymce configuration
  [vangheem]

- Fix #1071: AttributeError when saving theme settings
- Remove unused types_link_to_folder_contents setting
  [vangheem]

- Fix #817: When saving the filter control panel show a flash message with
  info on caching.
  [jcerjak]

- Remove Chrome Frame from ``X-UA-Compatible`` HTTP header as it's deprecated.
  [hvelarde]

- Fix mail controlpanel not keeping password field when saving
  [allusa]

- Remove trying to install plone.protect to global site manager
  as that is now handled by plone.protect
  [vangheem]

- Fix traceback style (closes `#1053`_).
  [rodfersou]

- Let plone-final import step also depend on the workflow step.
  Otherwise the plone-final step installs plone.app.discussion with an
  extra workflow, and then our own workflow step throws it away again.
  Closes `#1041`_.
  [maurits]

- Purge profile upgrade versions from portal_setup when applying our
  default CMFPlone:plone profile.  This signals that nothing has been
  installed yet, so dependencies will get reapplied instead of possibly
  upgraded.  This could cause problems mostly in tests.  Closes
  `#1041`_.
  [maurits]

- Fix image preview in TinyMCE editor when in modals.
  [Gagaro]


5.0rc3 (2015-09-21)
-------------------

- Fix i18n in accessibility-info.pt
  [vincentfretin]

- Resolve deprecation warnings about portal_url
  [fulv]

- Improve contrast for pending state when state menu active (closes `#913`_).
  [rodfersou]

- Fix buttons positions on resource registry (closes `#886`_).
  [rodfersou]

- Add missing file for ace-editor to edit XML files (closes `#895`_).
  [rodfersou]

- Remove empty options for Site Settings configlet (closes `#996`_).
  [rodfersou]

- Hide document byline viewlet by default.
  [esteele]

- Move portal property email_charset to the registry.
  [esteele]

- Fix `#950`_: Missing personal toolbar when expanding the horizontal toolbar
  [ichim-david]

- Make sure portal_actions are imported before default portlets.
  Fixes `#1015`_.
  [vangheem]

- Move calendar_starting_year and calendar_future_years_available to
  registry and Products.Archetypes.
  [pbauer]

- Use registry lookup for types_use_view_action_in_listings
  [esteele]

- Add view @@hero to be included by plonetheme.barceloneta with diazo.
  [pbauer]

- Fix `#991`_: improve contrast for pending state in tollbar.
  [pabo3000]

- remove unused code to create NavTree probably left from Plone 3.0 times
  and since a while handled by plone.app.portlets.

- add navigation root registry value
  [jensens]

- Implement new feed syndication using `NewsML 1 <http://iptc.org/standards/newsml-1/>`_,
  an IPTC standard that provides a media-type-independent, structural framework for multi-media news.
  [frapell, jpgimenez, tcurvelo, rodfersou]

- provide positive number validator
  [vangheem]

- Move external_links_open_new_window, redirect_links to the registry.
  [esteele]

- Remove invalid_ids portal property as it isn't used.
  [esteele]

- Fix `#963`_: respect icon visibility setting
  [vangheem]

- Fix `#935`_: Fix group membership form rendering when group can't be found.
  [esteele]

- Fix redirect for syndication-controlpanel.
  [pbauer]

- Add advanced-option to button "Add Plone Site" in ZMI.
  [pbauer]

- Fix `#952`_: Toolbar menu completely misplaced because of link duplication
  [ichim-david]

- Fix issue where some filter settings would not get saved and provide
  correct defaults
  [vangheem]

- Better default tinymce settings
  [vangheem]

- Give some padding at the bottom of the toolbar menu dropdowns
  [sneridagh]


5.0rc2 (2015-09-11)
-------------------

- Move login properties to the configuration registry.
  [esteele]

- Fix changing searchable in types-controlpanel.
  Fix `#926`_.
  [pbauer]

- Respect view-url in livesearch-results. Fixes `#918`_.
  [pbauer]

- Fix Livesearch for items without review_state (files and image). Fixes #915.
  [pbauer]

- Apply isURLInPortal fix from https://pypi.python.org/pypi/Products.PloneHotfix20150910
  [vangheem]

- Do not bother additional CRSF protection for addMember since all public
  users get same CSRF token and the method should be unpublished.
  See https://pypi.python.org/pypi/Products.PloneHotfix20150910
  [vangheem]

- Remove site properties that have been migrated to the registry.
  [esteele]

- fix `#862`_: Profile listing on site creation has alignment issues
  [ichim-david]


5.0rc1 (2015-09-08)
-------------------

- Remove deprecated global_defines.pt
  [esteele]

- Remove no-longer-used properties from portal_properties
  [esteele]

- Move footer and colophon out of skins
  [vangheem]

- pre-cook resources so we do not write on read for resources generation
  [vangheem]

- Turn robots.txt into a browser-view, fix link to sitemap.xml.gz, allow
  editing in site-controlpanel.
  Fixes `#604`_.
  [pbauer]

- Remove history_form, history_comparison templates.
  Remove now-empty plone_forms skins folder.
  [esteele]

- Remove no-longer-used images from portal_images.
  [esteele]

- Typo in delete modal configuration caused submission redirection errors
  [vangheem]

- Upgrade known core packages at the end of the Plone migration.
  [maurits]

- remove Products.CMFPlone.utils.isLinked function. Switch to using
  plone.app.linkintegrity's variant
  [vangheem]

- Fix error to allow site navigation if TinyMCE content_css setting is None
  [Gagaro]


5.0b4 (2015-08-23)
------------------

- fix `#350`_: "plone.app.content circular dependency on Products.CMFPlone" - this
  fixes the imports only, not on zcml/genericsetup level.
  [jensens]

- move Plone specific ``getDefaultPage`` (magic) code from plone.app.layout
  over to Products.CMFPlone. This avoids a circular dependency. Also its
  not really layout only related code.
  [jensens]

- Fix add-ons to be installed using CMFQuickInstaller (restore support
  for Extensions/Install.py)
  [datakurre]

- Rename showEditableBorder to showToolbar and deprecate using
  disable_border and enable_border for enable_toolbar and disable_toolbar
  [vangheem]

- Not using less variables in toolbar everywhere
  [vangheem]

- Fix link to documentation

- Rework timezone selection in @@plone-addsite.
  [jaroel]

- Rework language selection in @@plone-addsite.
  [jaroel]

- Turn @@tinymce-controlpanel ``content_css`` field into a list, so we can add
  several CSS URLs (useful when add-ons need to provide extra TinyMCE styles),
  and fix TinyMCE config getter so it considers the ``content_css`` value.
  [ebrehault]


5.0b3 (2015-07-20)
------------------

- show toolbar buttons on sitemap, accessibility and search pages
  [vangheem]

- log info after catalog rebuilt
  [vangheem]

- Renamed 'Zope Management Interface' to 'Management Interface'.
  [jaroel, aclark]

- Fix adding a new Plone site with country specific language. Refs `#411`_.
  [jaroel]

- fix plone-logged-in bundle not using global jquery for requirejs dependency and in
  weird cases causing select2 load errors in patterns(especially resource registry)
  [vangheem]

- Use new plone.app.theming policy API and delegate theme cache to plone.app.theming
  [gyst]

- Fix issue where site root syndication was giving 404s
  [vangheem]

- update time widget interval selection to be the same as Plone 4 time selection intervals
  [vangheem]

- use ajax_load in @@search when loading results dynamically, and add missing
  closing tag
  [ebrehault]

- better formatting of config.js
  [vangheem]

- Upload pattern uses the baseUrl to compute the upload URL, so this should
  always be the site root and not the current context
  [frapell]

- rewrite css files when saving customized files in the resource registry
  [vangheem]

- Update links to point to '@@overview-controlpanel'.
  Fixes `#573`_.
  [gforcada]

- Fix email validation of long domain names.
  [gotcha]

- fix syndication feed use of lead image as it was using wrong url
  [vangheem]

- add utility to get site logo
  [vangheem]

- fix issue where product upgrade did show an error status message
  [datakurre]

- fix casing on "First weekday" field on Date and Time control panel
  [vangheem]

- fix imaging control panel example format on description
  [vangheem]

- Add page title to resource registry
  [vangheem]

- Remove ramcache-controlpanel csrf test. Ramcache control panel has been
  moved to p.a.caching since ages. We will get rid of it.
  [timo]

- Add undeclared zope.cachedescriptors dependency.
  [timo]

- Do not require "Enable LiveSearch". This fixes `#558`_.
  [timo]

- Fix control panel titles. This fixes `#550`_, `#553`_, `#557`_.
  [timo]

- remove plone.app.jquerytools dependency
  [vangheem]

- fix bug where bundles would not get built properly with
  compile-plone-resources script when multiple resources
  were defined for a bundle
  [vangheem]

- do not require css to be defined for non-compilable bundles
  [vangheem]

- fix weird issue with selecting multiple links and images on a page
  while you are editing with tinymce
  [vangheem]

- updates to contact forms to make them more user friendly on submission
  [vangheem]

- include code plugin by default for TinyMCE
  [vangheem]

- Fix build reading browser cached files by appending random query
  param onto url. See `commit 2d3865805efc6b72dce236eb68e502d8c57717b6`_
  and `commit bd1f9ba99d1ad40bb7fe1c00eaa32b8884aae5e2`_.
  [vangheem]

- fix manage content type and group portlets link to have authenticator
  [vangheem]

- Convert manage-portlets.js into a pattern and make improvements on
  using the manage portlets infrastructure
  [vangheem]

- Remove dependency on plone.app.form and other formlib packages
  [tomgross]

- Remove plone.skip_links from the default set of viewlets in order to follow
  modern a11y methods and drop support for outdated ways [sneridagh]

- Change the name and link of 'Types' control panel to 'Content Settings' and
  '@@content-controlpanel' since there was confusion with the 'Dexterity
  Content Types' one [sneridagh]


5.0b2 (2015-05-13)
------------------

- Add social media settings control panel

- add ability to provide a css file for tinymce style formats
  [vangheem]

- fix plone-generate-gruntfile to compile each less resource
  separately
  [vangheem]

- provide image alignment styles for tinymce images
  [vangheem]

- Respect TinyMCE control panel settings
  [vangheem]

- enable/disable versioning behavior with settings in Types control panel
  [vangheem]

- Make ``typesToList`` read ``metaTypesNotToList`` from new p.a.registry settings.
  This fixes `#454`_.
  [timo]

- style tweaks to toolbar
  [pbauer]

- fix search form usability
  [vangheem]

- detect when changes are made to the legacy bundle through the interface
  so resources are re-built when they need to be
  [vangheem]

- fix some legacy import wonkiness. Inserting multiple times, insert-before
  and remove fixed
  [vangheem]

- make live search and search form give consistent results
  [vangheem]

- only show edit bar if user logged in
  [vangheem]

- fix error sending test email in Mail control panel
  [tkimnguyen]

- pat-modal pattern has been renamed to pat-plone-modal
  [jcbrand]

- Remove Products.CMFFormController dependency.
  [timo]

- Fix submission of tinymce control panel.
  [davisagli]

- Monkey patch SMTPMailer init method to pick up the mail settings from the
  registry instead of from the MailHost itself.
  [timo]

- Add `resource_blacklist` attribute to resource registry importer, to
  allow filtering of known bad legacy resource imports.  Filter js from
  plone.app.jquery.
  [alecm]

- Fix broken "Installing a third party add-on" link
  [cedricmessiant]

- Fix folder contents button disappeared act
  [vangheem]

- Fix resource registry javascript build
  [vangheem]

- Move `plone.htmlhead.links` viewlet manager after `plone.scripts`,
  because the former is sometimes used to include scripts that depend on
  the latter.
  [davisagli]

- Change the order of the plonebar user menu and move the plone.personal_bar
  viewlet to the last position due to accessibility issues on having it being
  the first element.
  [sneridagh]

- We only support `utf-8` site-encoding at the moment
  [tomgross]


5.0b1.post1 (2015-03-27)
------------------------

- Packaging fix, no code changes.
  [esteele]


5.0b1 (2015-03-26)
------------------

- Add tests for configuring encoding of user registration or
  forgotten password emails.
  [davidjb]

- Pass email encoding to forgotten password email template.
  [davidjb]

- Pass mail ``Content-Type`` to mailhost when sending forgotten password
  emails.
  [davidjb]

- Move security control panel to CMFPlone. Fixes `#216`_.
  [jcerjak, timo]

- Remove ``create_userfolder`` from addPloneSite factory, it is not used
  anymore.
  [jcerjak]

- Read security settings from the registry instead of portal properties.
  [jcerjak,timo]

- Fix tests for plone.app.contenttypes unified view names, which uses
  ``listing_view`` for Folder and Collection types.
  [thet]

- Remove ``selectable_views`` from ``properties.xml``, which isn't used
  anywhere anymore.
  [thet]

- Remove the remaining ``Topic`` entry in ``default_page_types`` from
  ``propertiestool.xml``. This setting is now done in
  ``plone.app.contenttypes`` respectively ``Products.ATContentTypes``.
  [thet]

- Add __version__ attribute to __init__.py. This allows us to retrieve the
  current Plone version with 'Products.CMFPlone.__version__'. Even though this
  is no official standard, many packages in the Python standard library provide
  this.
  [timo]

- Replaced the legacy mark_special_links javascript with a
  corresponding mockup pattern.
  [fulv]

- remove plone_javascript_variables.js as necessary values
  are provided on body tag and pattern options
  [vangheem]

- fix bootstrap css bleeding into global namespaces
  [vangheem]

- add recurrence pattern
  [vangheem]

- add history support for folder contents
  [vangheem]

- Merge plone.app.search here
  [vangheem]

- Extended ulocalized_time for target_language
  [agitator]

- Caching for ``@@site-logo``.
  [thet]

- Support for portal site logos stored in the portal registry by uploading via
  the site control panel. Add a ``@@site-logo`` view for downloading the logo.
  [thet]

- Fix the resource registry to save the automatically generated filepath to the
  compiled resource on the bundle object after compilation. The filepath is
  always in the '++plone++static/' namespace. This fix makes custom bundles
  actually includable.
  [thet]

- Get icon from layout_view instead of plone_view.
  [pbauer]

- Fix contentViews (tabs) markup for Plone 5.
  [davisagli]

- Rename syndication-settings to syndication-controlpanel. Keep the old view registration for backwards compatibility.
  [timo]

- Added a link for the advanced 'Create a Plone site' screen to the Plone overview.
  [jaroel]

- Fixed the label for 'Example content' in the advanced 'Create a Plone site' screen.
  [jaroel]

- Move markup control panel to CMFPlone. Fixes `#220`_.
  [djay, thet]

- Use jstz to set default portal_timezone in @@plone-addsite.
  [instification]

- Make inline validation of AT multiple selection widget work.
  [gbastien]

- Make sure compiling resources does not commit transaction prematurely.
  [davisagli]

- Adding the option to configure a bundle from the diazo manifest file.
  [bloodbare]

- Move the controlpanel overview from plone.app.controlpanel into this package
  Fixes `#290`_.
  [khink]

- PLIP 10359: Migrate usergroups controlpanel to ``z3c.form`` and move it from
  plone.app.controlpanel to Products.CMFPlone. Fix and extend tests and add
  robot tests.
  [ferewuz]


5.0a3 (2014-11-01)
------------------

- folder_position script: make position and id optional.  Default
  position to 'ordered' and id to None, which means: do nothing.
  plone.folder 1.0.5 allows this, making it possible to simply reverse
  the current sort order by using reverse=False.
  [maurits]

- Fix JS resource viewlet HTML syntax error.
  [rpatterson]

- Fix resource bundle expressions.  They weren't being checked at all and
  reversed the condition if they had been.  Also move caching of the cooked
  expressions out of the DB and into a RAM cache.
  [rpatterson]

- Fix endless resource dependency loop when depending on a bundle that also has
  a dependency.
  [rpatterson]

- reduce deprecation warnings to use plone_layout and not plone_view for
  certain method calls in order to make debugging of robottests easier:
  w/o it shows 1000ds of extra lines in html report.
  [jensens]

- type controlpanel: Resolved problem with workflow selection form as it
  was breaking if state title had non-ascii characters. see also
  https://github.com/plone/plone.app.controlpanel/pull/26
  [lewicki, jensens]

- Minor overhaul of CatalogTool.py - no feature changes!
  Optimizations and better readable code for indexer
  ``allowedRolesAndUsers``: now using a set.
  Change if/elif/else to oneliner boolean expression in ``is_folderish``
  indexer.
  Usage of AccessControl 3 style decorators for security declarations.
  Minor reformattings to make code-analysis happy.
  [jensens]

- Removed some javascripts: fullscreenmode.js, dragdropreorder.js,
  styleswitcher.js, select_all.js, collapsibleformfields.js

- PLIP 13260: Migration cut, copy and paste into browser views.
  [saily]

- Abstract the search form and livesearch action URLs making it easier to
  extend the search portlet with custom views or other actions.
  [rpatterson]

- Fix JavaScript to work with recent jQuery (>= 1.9) versions.
  [thet]

- Small scoping fix in locking js code
  [do3cc]

- PLIP 13260: Migrate author page to browser views/z3c.form (issue `#78`_)
  [bosim]

- Integration of the new markup update and CSS for both Plone and Barceloneta
  theme. This is the work done in the GSOC Barceloneta theme project.
  [albertcasado, sneridagh]

- Created new viewlet manager for holding main navigation for a more semantic
  use of it. Move the global sections viewlet into it.
  [albertcasado]

- New toolbar markup based in ul li tags.
  [albertcasado, bloodbare, sneridagh]

- Update <div id="content"> in all templates with <article id="content">
  [albertcasado]

- PLIP 14261: New resource registries.
  [bloodbare, vangheem, robgietema, et al]


5.0a2 (2014-04-20)
------------------

- Advertise the migration of content to dexterity after a successful
  upgrade to Plone 5.
  [pbauer]

- Strip leading & trailing spaces from id and title in rename-form.
  See https://dev.plone.org/ticket/12998, https://dev.plone.org/ticket/12989,
  https://dev.plone.org/ticket/9370, https://dev.plone.org/ticket/8338
  [pbauer]

- Fix incorrect use of dict get method in CatalogTool.search, introduced
  by PloneHotfix20131210 (issue 195)
  [fulv]

- Added timezone selection to add site page
  [pysailor, yenzenz]

- Added date date and time controlpanel (moved over from plone.app.event).
  [yenzenz. thet]

- Remove DL/DT/DD's from portal messages, portlet templates and others.
  Fixes `#153`_, `#163`_.
  [khink]

- PLIP 13260 remove templates and form scripts for
  ``select_default_page`` and ``select_default_view`` because they got
  migrated to browser views. Fix tests for that and remove legacy tests.
  See `#90`_.
  [saily]

- PLIP 13260: Migration contact-info to ``z3c.form`` and make it highly
  customizable.
  [timitos, saily]


5.0a1 (2014-03-02)
------------------

- remove quickinstall control panel form since a new one was moved to
  plone.app.controlpanel
  [vangheem]

- Add 'warning' and 'error' status message types to the test_rendering
  view.
  [esteele]

- Update the front-page links.
  [esteele]

- In plone-overview view, we can now see Plone sites which are contained into
  Zope folder.
  [bsuttor]

- Make Plone tool read the exposeDCMetaTags from p.a.registry instead of
  of the site properties.
  [timo]

- Hide plone.app.registry install profile in the add-ons control panel.
  [esteele]

- Removed spamProtect.py script, since it doesn't offer real protection.
  [davisagli]

- Moved the member search form to plone.app.users
  [pabo3000]

- PLIP #13705: Remove <base> tag.
  [frapell]

- merge hotfixes from 20131210
  [vangheem]

- handle plone.app.textfield RichTextValue objects in syndication. Should
  fix syndication with plone.app.contenttypes.
  [vangheem]

- FolderFeed adapter now takes into account the limit property when displaying
  the RSS feed just like the other adapters do
  [ichim-david]

- Remove the portal_calendar tool and the dependency on CMFCalendar.
  [davisagli]

- Remove the plone_deprecated skin layer.
  [gforcada, davisagli]

- Moved portal_factory and portal_metadata from Products.CMFPlone to
  Products.ATContentTypes (PLIP #13770)
  [ale-rt]

- Remove the portal_interface tool.
  [ale-rt]

- Remove the portal_actionicons tool.
  [davisagli]

- Remove ownership_form and change_ownership script, which were not used.
  [davisagli]

- Convert author_feedback_template and accessibility_info to browser views.
  [bloodbare]

- Move calendar_macros and jscalendar to Products.Archetypes.
  [bloodbare]

- Remove plonetheme.classic from the package dependencies and the default
  extension profile, since it will not ship with Plone 5.
  [timo]

- Move docs/CHANGES.txt to CHANGES.rst.
  [timo]

- Replace deprecated test assert statements.
  [timo]

- Add a dependency on plone.app.theming. Install by default.
  [esteele]

- Drop dependency on plonetheme.classic.
  [esteele]

- Remove old logo.jpg. Use logo.png from Sunburst.
  [esteele]

- Inline validation JavaScript for z3c.form only sends request when
  field name can be obtained from DOM for a widget (#13741).
  [seanupton]

- Add use_uuid_as_userid site property.
  Part of PLIP 13419.
  [maurits]

- Let set_own_login_name use the update(Own)LoginName method from PAS.
  Part of PLIP 13419.
  [maurits]

- recently_modified and recently_published respects allow anonymous to view
  about setting
  [vangheem]

- Return a 404 instead of "AttributeError: (dynamic view)" if a user attempts to
  view a still-temporary PortalFactory item.
  [esteele]

- Ensure that initial_login is set to True when a user first logs in.
  [taito]

- Merged PLIP #12198: Depend on Chameleon (five.pt) as a faster page template
  engine.
  [davisagli]

- make extensionprofiles selection part of 'advanced' in plone-addsite
  [jaroel]

- enable syndication on plone.app.contenttypes collection
  [vangheem]

- fix syndication settings to not write on read
  [vangheem]

- fix wrong download url for podcast syndication
  [Rudd-O]

- Merged PLIP #12344: Use Dexterity-based core content types.

  * Avoid including ATContentTypes and Archetypes as a dependency.
  * Install the plone.app.contenttypes profile for new sites.

  [davisagli et al]

- Merged PLIP #13270: Move presentation mode out of core.
  If the feature is still desired, use the plone.app.s5slideshow add-on.
  [davisagli]

- Add "plone-5" ZCML feature. Add-ons can register
  ZCML for Plone 5 only using zcml:condition="have plone-5"
  [davisagli]

- Plone's javascript is now developed as part of the Plone mockup
  (http://github.com/plone/mockup) and is included as a compiled
  bundle.
  [davisagli]

- Removed portal_interface tool (PLIP #13770)
  [ale-rt]

- Removed kss_field_decorator_view support
  [maurits, jaroel]

5.0.0 (unreleased)
------------------

- Plone's javascript is now developed as part of the Plone mockup
  (http://github.com/plone/mockup) and is included as a compiled
  bundle.
  [davisagli]

- Removed portal_interface tool (PLIP #13770)
  [ale-rt]

- Removed kss_field_decorator_view support
  [maurits, jaroel]

- Remove CMFDefault dependency
  [tomgross]

- Sub-sort timezone by label, not language code when adding a site
  [instification]


4.3.3 (unreleased)
------------------

- Added a method toLocalizedString to @@plone view,
  on the model of toLocalizedTime,
  to get a localized string rendering a size from an integer.
  Use it on image view.
  [thomasdesvenain]

- Move propertysheet imaging_properties and the corresponding
  utilities from plone.app.imaging to Products.CMFPlone.
  https://github.com/plone/plone.app.contenttypes/issues/82
  [pbauer]

- Ensure ``object_rename`` script has ``_`` message factory available
  to prevent error when unauthorized.
  [davidjb]

- Fix issue with the search js in sharing page where the user needed to check
  twice a checkbox to assign a role after a search.
  [vincentfretin]

- Catch missing userid on mail_password form, and treat is as
  an empty userid. That way the user gets a helpful message.
  [do3cc]

- Fixed item.body call in search-rss.pt so now works even when
  item.body is an AcquisitionWrapper.
  [alecghica]


4.3.2 (unreleased)
------------------

- Applied security fixes from PloneHotfix20130618:

  - Protected methods on the ZCatalog.
  - Added missing module security declarations.
  - Sanitize url in isURLInPortal.
  - Check 'Set own password' permission in mailPassword.
  - Prevent the Zope request from being traversed.
  - Protected sendto method.
  - Sanitize input to spamProtect script.

  [davisagli]

- Get ``portal_discussion`` properly with ``getToolByName``.
  [maurits]

- Fix dependency ordering problem with plone-final import step.
  [davisagli]

- remove bbb-kss.css from css registry registration
  [vangheem]

- Stop unload-protection from popping up needlessly if tinyMCE is used on tabbed forms
  [href]


4.3.1 (2013-05-30)
------------------

- Some text/* mime types should be Files, not Documents.
  [rpatterson]

- Remove reference to unimplemented 'make_private' transition in
  simple_publication_workflow.
  [danjacka]

- Fail nicely when pasting a deleted item (https://dev.plone.org/ticket/13337)
  [khink]

- Add a 'max_tabs' option to form-tabbing.js to allow changes to the number of
  tabs displayed before the script uses a dropdown instead.
  [esteele]

- register search_rss only for site root
  [vangheem]

- jquery-integration.js gets disabled during the upgrade to Plone 4.3. Make sure
  we do so for new sites as well.
  [esteele]

- Fix commas in kss-bbb.js since IE7/8 is sensitive [vangheem]

- Re-enable forgotten tests [kiorky]

- Fail nicely when userid is not provided to mail_password script.
  [esteele]

- Do not display text file content if it is empty.
  [thomasdesvenain]

- Add distinct classes for live search links.
  Add id for image details.
  [cedricmessiant]

- update registerPloneFunction call in login.js (deprecated)
  [toutpt]

4.3 (2013-04-06)
----------------

- Fix attribute values in selector expressions of  mark_special_links.js.
  [mathias.leimgruber]

- Add indexer for location so metadata is included in catalog
  [vangheem]

- Fix rss 2.0 not providing actual link
  [vangheem]

- Prevent js inline validation call to /at_validate_field for .blurrable
  inputs that do not have AT field data validation attributes. This
  avoids cluttering the error logs with useless at_validate_field
  errors for fields that just happen to have .blurrable class.
  [mcmahon]

- Test for #7627 (https://dev.plone.org/ticket/7627)

4.3rc1 (released)
-------------------

- add overlay for folder default page folder factories link
  [vangheem]

- add sitemap.xml.gz to robots.txt fixes https://dev.plone.org/ticket/13319
  [vangheem]

- update add site, overview and upgrade templates to use absolute urls
  to reference css and image resources so it works with virtual hosted
  sites to sub-folders fixes #11153
  [vangheem]

- Allow the Content-Type header to be set in registered_notify_template.pt
  [esteele]

- Extract RegistrationTool's sending of registration emails so that it can be
  more easily overridden.
  [esteele]

- bump profile version
  [vangheem]

- Add event to fix products installed with latest keyword
  activated by default. Event finds new products installed with
  the latest keyword and updates them to the last profile version.
  [eleddy]

- Add event to trigger when a reordering is happening. Without this
  collective.solr and maybe other alternative indexes are kind of lost.
  Backport from 4.2.x
  [do3cc]

- Robot Framework based acceptance tests added.
  [timo]

- Remove comment form overlay which was only used for the old
  pre-plone.app.discussion reply form.
  [timo]


4.3b2 (2013-01-17)
------------------

- removing ``plone_ecmascript/test_ecmascripts.pt`` since its not working and
  since its not being ran by out test suite.
  [garbas]

- Call searchUsers with the 'name' argument instead of 'login'.
  'name' is the officially supported way according to the PAS interface.
  [maurits]


4.3b1 (2012-01-02)
------------------

- Changes to dependencies when creating a new site (plone-final) to fix
  #11997.
  [keul]

- Generate valid atom feeds
  [lentinj]

- Fix quoted atom.xml feed syndication content type to "html".
  [elro]

- Add various security fixes based on PloneHotfix20121106.
  [davisagli]

- Fix RegistrationTool testPasswordValidity method. See
  https://dev.plone.org/ticket/13325
  [vipod]

- Fix form_tabbing.js so it stays on the same fieldset when an Archetypes
  edit form is submitted and returns to itself.
  [davisagli]

- Use the 'OFS.ObjectManager.bad_id' pattern in 'PloneTool.BAD_CHARS'.
  This allows names containing '@' to pass 'check_id'.
  [elro]

- Pass minute_step to date_components_support_view.result(). See
  https://dev.plone.org/ticket/11251
  [gbastien]

- Improve error handling on paste action. If it is a real error, the
  error gets shown and logged.
  [do3cc]

- Fix sitemap rendering. No longer uses portlet_navtree_macro.pt from
  the plone_deprecated skin, but a browser view template with much
  simplified logic.
  [danjacka]

- Revealed hidden features for sorting folders (#11317).
  [keul]

- Don't swallow exceptions on object_paste and folder_paste (#9365).
  [gaudenz]

4.3a2 (2012-10-18)
------------------

- Use prefixed ids for popup overlays
  [maartenkling]

- Fix compatible hide fieldset legend for IE6/7/8 in form_tabbing.js
  [maartenkling]

- Add an animated indicator of AJAX loading via Javascript.
  It is now called #ajax-spinner and is no longer added in main_template.
  [davisagli]

- Remove Plone's dependency on KSS. plone.app.kss is now an optional add-on.
  Functionality that used to be provided using KSS has been reimplemented.
  [esteele, vangheem, cah190, davisagli]

- Do not block right-side portlets in Members folder on site creation.
  This fixes https://dev.plone.org/ticket/10764
  [polyester]

- Fix prefs_install_product_readme so files with non-ascii characters are
  rendered. This fixes https://dev.plone.org/ticket/12342
  [ericof]

- Fix StringIO module security so it can still be imported from restricted
  code in Zope 2.13.17+.
  [davisagli]

- Filter out non existing types in getUserFriendlyTypes.
  This avoids an error on the search form when a no longer existing
  portal_type is still in the catalog.
  [maurits]

- Declare Plone's dependency on Pillow.
  [davisagli]

- Merge syndication plip 12908
  [vangheem]

- Add body class depth registry field
  [vangheem]

- Check if an item is locked before attempting to delete. Refs #11188
  [eleddy]

- We can safely move the MAX_TITLE to 50 and even move up MAX_DESCRIPTION 150 refs #11321
  [maartenkling]

- Remove inline styles, they do nothing, add class so someone can style it when they like refs #12438
  [maartenkling]

- Show forget password when entering wrong credentials refs #12463
  [maartenkling]

- Remove h3 to make consistent html refs #11344
  [maartenkling]

- Fix 'Add New' on Users/Groups Overviews shows overlay when clicking anywhere in form #12201
  [maartenkling]

- Fix events_listing #12477
  [maartenkling]

- Fix form_tabbing, to stay on current tab on submitting form
  [maartenkling]


4.3a1 (2012-08-31)
------------------

- Hide 'plone.resource' and 'collective.z3cform.datetimewidget' from the
  site factory screen. These are only useful as dependencies of other packages.
  [optilude]

- Define a ZCML feature called `plone-43` in addition to the existing ones.
  [thet]

- Deprecated getSiteEncoding and changed occurrences to hardcoded `utf-8`
  [tom_gross]

- zope.globalrequest is a required dependency on tests.
  [hvelarde]

- Make sure the ResourceRegistries registry setting is created for new sites.
  [davisagli]

- Searches ignore accents.
  PLIP http://dev.plone.org/ticket/12110
  [thomasdesvenain]

- IE critical fix on toggle select and form submit helpers.
  [thomasdesvenain]

- Fixed javascript injections on jquery.highlightsearchterms.js
  [gborelli]

- Tweak rules for `sortable_title`. So far we took the first 70 chars and
  zero-padded numbers to six digits. Now we zero-pad to four digits and take
  the first 30 and the last 10 characters, thus saving space while still
  distinguishing long titles which only differ at the end, like imported
  file or image names.
  [hannosch]

- PEP 8 (ignoring W602, E203, E241, E301, E501 and E701).
  [pbdiode, hvelarde]

- Add 'displayPublicationDateInByline' to site properties property sheet in
  order to finish PLIP #8699: Display publication date in author byline.
  [vipod]

- Deprecated aliases were replaced on tests.
  [hvelarde]

- Don't register the plone_deprecated skin layer. These items are no
  longer supported as part of Plone and remain here temporarily as a
  convenience to those who may need to move them into their own
  packages.
  [davisagli]

- Ensure multiple tabbed forms on the same page work when number of
  tabs is greater than threshold.
  [davidjb]

- Remove deprecated `jq` reference from form tabbing JavaScript.
  [davidjb]

- Remove incorrect line of form tabbing JavaScript which broke
  forms with more than 6 tabs.
  Fixes https://dev.plone.org/ticket/12877
  [davidjb]

- accessibility improvements for screen readers regarding "more" links,
  see http://dev.plone.org/ticket/11982
  [rmattb, applied by polyester]

- Fix an outdated "Send this" form handler property reference.
  [rossp]

- removed search_form-template form plone_deprecated-skin. Use
  collective.searchform if you need this functionality.
  [tom_gross]

- Use plone.batching for all batches (PLIP #12235)
  [tom_gross]

- Re-apply PLIP 10901 to table_sort.js, fixing a bug with reversing sort
  on the first column.
  [mj]

- support a PAS plugin for validating passwords
  PLIP http://dev.plone.org/ticket/10959
  [djay75]

- Make redirection_view/attempt_redirect fall back to nothing in
  default_error_message template. If plone.app.redirector gets a URL with
  special characters, OOBTree.get raises a UnicodeDecodeError and the template
  fails. This fixes http://dev.plone.org/ticket/12976.

- Channel link in RSS feed now points to the un-syndicated content for the RSS feed,
  instead of the portal root.
  [patch by pydanny, applied by kleist]

- Removed unused "localTimeFormat", "localLongTimeFormat", and "localTimeOnlyFormat"
  from "/portal_properties/site_properties".
  Fixes https://dev.plone.org/ticket/11171.
  [kleist]

- CatalogTool.py, PloneBatch.py, PloneFolder.py, PloneTool.py, Portal.py:
  Don't use list as default parameter value.
  [kleist]

- Use configuration registry to override translation of date format,
  or fall back to ISO style as last resort. Fixes http://dev.plone.org/ticket/11171
  [kleist]



4.2.1.1 (2012-08-23)
--------------------

- Fixed i18n of image view improvement introduced in 4.2.1.
  [vincentfretin]

- Ensure some transient dependencies don't vanish in the 4.2 series,
  just because some libraries get updated and nobody declares the
  dependency anymore.  Same as in the Plone package:
  zope.copypastemove, zope.app.component, zope.app.container,
  zope.app.publisher.
  [maurits]


4.2.1 (2012-08-11)
------------------

- Fix: do not display 'file content' on a file view if there is no file.
  [thomasdesvenain]

- Improve image view:

    - Add a download button.
    - Display View button only if image is a web format (jpeg, png, gif...)

  [thomasdesvenain]

- zope.globalrequest is a required dependency on tests.
  [hvelarde]

- Remove content-core ID from login_form. This removes the duplicate ID
  that occurs on a page when using the login overlay.
  This fixes https://dev.plone.org/ticket/12439
  [cwainwright]


4.2.0.1 (2012-07-02)
--------------------

- Add docstring to SkinTool's method to allow them being called from the ZMI.
  [erral]


4.2 (2012-06-29)
----------------

- Add upgrade step to install the CMFEditions component registry bases
  modifier.
  [rossp]

- Make redirection_view/attempt_redirect fall back to nothing in
  default_error_message template. If plone.app.redirector gets a URL with
  special characters, OOBTree.get raises a UnicodeDecodeError and the template
  fails. This fixes http://dev.plone.org/ticket/12976.
  [timo]

- Fix jquery.highlightsearchterms.js to not render arbitrary js.
  [vangheem]


4.2rc2 (2012-05-31)
-------------------

- Check the existence of a portal_type attribute before accessing it to construct
  navigation URLs. This avoids an exception when constructing breadcrumb navigation
  for search results if the result is a 'Discussion Item' as the parent Conversation
  object does not have a portal_type attribute.
  [gaudenz]

- When adding, changing or removing skins, automatically recook all resource
  registries, to keep theme bundles in-sync. This mirrors the event subscriber
  support used in plone.app.registry for the same purpose.
  [hannosch]

- Let the RR export/import steps depend on the skins tool and
  plone.app.registry steps, as either of them might create new theme bundles
  [hannosch]

- Hide Kupu base profile on Plone site creation screen.
  [hannosch]

- Accessibility improvements for screen readers regarding "more" links, see
  http://dev.plone.org/ticket/11982
  [rmattb, applied by polyester]


4.2rc1 (2012-05-07)
-------------------

- Fix an outdated "Send this" form handler property reference.
  [rossp]

- removed search_form-template form plone_deprecated-skin. Use
  collective.searchform if you need this functionality.
  [tom_gross]

- Use plone.batching for all batches (PLIP #12235)
  [tom_gross]

- Re-apply PLIP 10901 to table_sort.js, fixing a bug with reversing sort
  on the first column.
  [mj]

- Stop filtering folder_listing to the types from
  @@plone_portal_state/friendly_types, since that excludes non-searchable
  types rather than non-listable types.
  [davisagli]

- PloneControlPanel's enumConfiglets no longer returns invisible configlets.
  [esteele]

- Hide the (old) Collections control panel by default for new sites.
  [esteele]

- Apply duplicate-submit protection to inputs of type 'image' in addition
  to type 'submit'.
  [davisagli]

- Use getId() instead of title_or_id() for displaying which items get deleted,
  to avoid unicode error
  Fixes https://dev.plone.org/ticket/12765
  [spereverde]

- Allow form tabbing to be used across different DOM documents.
  [rossp]

- Hide left column in prefs_main_template when user does not have access to
  configlets.
  Fixes https://dev.plone.org/ticket/12572
  [gotcha]

- Hide left column in prefs_main_template when user does not have access to
  configlets.
  Fixes https://dev.plone.org/ticket/12572
  [gotcha]

- Make MigrationTool.coreVersions() check for Pillow as well as PIL and
  PILwoTK. Version will report as "PIL 1.7.6 (Pillow)". Closes
  http://dev.plone.org/ticket/12158
  [smcmahon]

- Decode id and bad characters in check_id script with default_encoding to
  prevent UnicodeDecodeError when bad characters contains non-ascii letters.
  Fixes https://dev.plone.org/ticket/12525
  [pingviini]

- Add keyword 'latest' to metadata.xml's version tag, which then looks for
  the highest numbered profile that is registered and pins that to the
  upgrade step. This means that the version field in metadata.xml only
  has to be set to 'latest' once and then it automatically searches for
  the highest numbered profile.
  [eleddy]


4.2b2 (2012-02-09)
------------------
- Changed link from search to @@search for the "More" link in livesearch_reply.
  [vincentfretin]

- Notify ObjectModifiedEvent when a content title is modified
  through action > rename.
  Fixes http://dev.plone.org/ticket/12460
  [thomasdesvenain]

- Fixed some mail tests in combination with five.pt.
  [maurits]

- Do not display the author contact form when the logged in user does
  not have an email address.
  Fixes http://dev.plone.org/ticket/12258
  [maurits]

- When password mail is sent, SMTPException will now be detected
  if named parameter "immediate" passed to RegistrationTool.mailPassword().
  Fixes http://dev.plone.org/ticket/6047 (together with a commit for
  plone.app.controlpanel::usergroups.py)
  [kleist]


4.2b1 (2011-12-05)
------------------

- Define a ZCML feature called `plone-42` in addition to the existing
  `plone-4` and `plone-41` to be used in conditional ZCML registrations.
  [vincentfretin]

- Allow "Site Administrator to add keywords"
  [kleist, suggested by keul]

- IE critical fix on toggle select and form submit helpers.
  [thomasdesvenain]

- Fixed the two high priority scenarios (global sections viewlet and nav
  portlet) of http://dev.plone.org/ticket/11189.
  [fulv]

- Call the view to unlock an item on unload synchronously, so that the
  call succeeds on Webkit browsers. This closes
  http://dev.plone.org/ticket/7885
  [davisagli]

- Remove unneeded kss debugging code
  [jfroche]

- Allow users with the Manage Users permission to change the login
  name of other users; specifically this allows them to change the
  email address when this is used as login name.
  Fixes http://dev.plone.org/plone/ticket/11255
  [maurits]

- Removed the 'What' row in the event view that displayed the
  keywords; this is already handled by the keywords viewlet.
  Fixes http://dev.plone.org/plone/ticket/10818
  [maurits]

- Make control panel action GS export return actions alphabetically since
  there is no other natural ordering.
  [ggozad]

- Fixed folder_listing template
  so that listing macro can be used outside of folder_listing.
  [thomasdesvenain]

- Fix PloneTool.changeOwnershipOf to not pass MemberData to the underlying
  Owned.changeOwnership, but a plain User object only.
  [stefan]

- Fixed bug that treated ids of objects outside the portal, but on the
  acquisition path, as reserved.
  Fixeѕ https://dev.plone.org/ticket/10547
  [rochecompaan]


4.2a2 - 2011-08-25
------------------

- AuthenticatedUsers group is used for local roles etc, and is not the same as
  Authenticated role. Thus, it can not be optimized away in catalog queries.
  [tesdal]

- getFolderContents only sets b_size if batching is true.
  [do3cc]


4.2a1 - 2011-08-08
------------------

- Added hidden year/month/day/hour/minute/ampm labels to calendar macros.
  Part of a form accessibility cleanup.
  [smcmahon]

- Removed registration of the input-label.js from the portal_javascript tool.
  Those with a desperate need to support the 'placeholder' text functionality
  in the obsolete browsers are free to re-register the script in their own
  instances.
  [spliter]

- Deprecated input-label.js — instead we are using the HTML5 'placeholder'
  attribute on the input fields.
  [spliter]

- Deprecated IEFixes.css after we have introduced Modernizr and removed it's
  GS registration. References http://dev.plone.org/plone/ticket/11300
  [spliter]

- Added Modernizr 2 library.
  References http://dev.plone.org/plone/ticket/11300
  [spliter]

- Switch to HTML5 doctype. References http://dev.plone.org/plone/ticket/11300
  [spliter]

- Include plone.app.collection and related packages.
  Refs http://dev.plone.org/plone/ticket/10902
  [esteele]


4.1.6 (2012-06-27)
------------------

- Add keyword 'latest' to metadata.xml's version tag, which then looks for
  the highest numbered profile that is registered and pins that to the
  upgrade step. This means that the version field in metadata.xml only
  has to be set to 'latest' once and then it automatically searches for
  the highest numbered profile.
  [eleddy]

- Accessibility:  added an id="Creator" for the <input> field by the same name
  on the search form, so that the corresponding <label> can associate with it
  in the case where showAuthors is None.

- Make redirection_view/attempt_redirect fall back to nothing in
  default_error_message template. If plone.app.redirector gets a URL with
  special characters, OOBTree.get raises a UnicodeDecodeError and the template
  fails. This fixes http://dev.plone.org/ticket/12976.
  [timo]


4.1.5 (2012-04-18)
------------------

- Stop filtering folder_listing to the types from
  @@plone_portal_state/friendly_types, since that excludes non-searchable
  types rather than non-listable types.
  [davisagli]

- PloneControlPanel's enumConfiglets no longer returns invisible configlets.
  [esteele]

- Use getId() instead of title_or_id() for displaying which items get
  deleted, to avoid unicode error
  Fixes https://dev.plone.org/ticket/12765
  [spereverde]

- Hide left column in prefs_main_template when user does not have access to
  configlets.
  Fixes https://dev.plone.org/ticket/12572
  [gotcha]

- Re-apply PLIP 10901 to table_sort.js, fixing a bug with reversing sort
  on the first column.
  [mj]


4.1.4 (2012-02-08)
------------------
- Catch KeyError on 'userid' that occurs when mail_password is
  accessed directly (without 'userid' in the request). Return
  mail_password_form.
  [brayt]

- Notify ObjectModifiedEvent when a content title is modified
  through action > rename.
  Fixes http://dev.plone.org/ticket/12460
  [thomasdesvenain]

- Fixed some mail tests in combination with five.pt.
  [maurits]

- Do not display the author contact form when the logged in user does
  not have an email address.
  Fixes http://dev.plone.org/ticket/12258
  [maurits]


4.1.3 (2011-11-28)
------------------

- IE critical fix on toggle select and form submit helpers.
  [thomasdesvenain]


4.1.2 (10/13/2011)
------------------

- Fixed the two high priority scenarios (global sections viewlet and nav
  portlet) of http://dev.plone.org/ticket/11189.
  [fulv]

- Allow users with the Manage Users permission to change the login
  name of other users; specifically this allows them to change the
  email address when this is used as login name.
  Fixes http://dev.plone.org/plone/ticket/11255
  [maurits]

- Re-enable the getObjPositionInParent index in the portal_atct tool.
  Fixes http://dev.plone.org/plone/ticket/11151
  [davisagli]

- Removed the 'What' row in the event view that displayed the
  keywords; this is already handled by the keywords viewlet.
  Fixes http://dev.plone.org/plone/ticket/10818
  [maurits]

- Fix PloneTool.changeOwnershipOf to not pass MemberData to the underlying
  Owned.changeOwnership, but a plain User object only.
  [stefan]


4.1.1 (2011-09-21)
------------------

- Fixed folder_listing template
  so that listing macro can be used outside of folder_listing.
  [thomasdesvenain]

- AuthenticatedUsers group is used for local roles etc, and is not the same
  as Authenticated role. Thus, it can not be optimized away in catalog queries.
  [tesdal]

- getFolderContents only sets b_size if batching is true.
  [do3cc]

4.1 - 2011-07-12
----------------

- Make the ``plone-final`` import step dependent on ``rolemap`` to
  prevent some hard-to-debug add-on product related issues.
  Closes http://dev.plone.org/plone/ticket/11997;
  [MatthewWilkes]

- Use ``transaction.savepoint`` instead of ``transaction.begin`` in
  ``isLinked``;
  closes http://dev.plone.org/plone/ticket/7784; does not reopen
  http://dev.plone.org/plone/ticket/6666 probably because we use fixed version
  of ZEO
  [gotcha]

- Fix: content status history form entries are not batched because there is
  no batch navigation management on this page,
  so that all selected elements from folder contents are displayed.
  [thomasdesvenain]

- Optimized: Huge optimization of calendar_formfield.js under ie8 and lower.
  Gain of 50% on js execution on a large page.
  [thomasdesvenain]

4.1rc3 - 2011-06-02
-------------------

- Apply patches to prevent exploitation of CVE-2011-1948 (Hotfix 20110531.)
  [elro]

- In actions.xml, use object_url for the object_buttons.
  Fixes http://dev.plone.org/plone/ticket/11733.
  [WouterVH]

- Set Language to 'all' to list content in all languages when listing a
  worklist's contents (workflow) to support LinguaPlone better.
  [mj]

- Set appropriate cache headers on createObject redirects to prevent caching
  by proxy servers.
  [elro]

- Added "X-Theme-Disabled" response header to failsafe_login_form to disable
  Diazo/plone.app.theming.
  [elro]

- Fixed PloneBatch to work for non-lazy sequences.
  [hannosch]

- Explicitly load the `configure.zcml` from `plone.app.upgrade`, so the upgrade
  steps are loaded in `plone.app.testing` based test layers.
  [hannosch]

- Define a ZCML feature called `plone-41` in addition to the existing `plone-4`
  to be used in conditional ZCML registrations.
  [hannosch]

- Avoid registering CMFDefault's upgrade steps, as they are not useful in Plone.
  [hannosch]

4.1rc2 - 2011-05-21
-------------------

- Fixed PloneBatch class to handle limited result sets correctly. This closes
  http://dev.plone.org/plone/ticket/11733.
  [hannosch]

- Hide datepicker icon for date widget if plone.jscalendar is not loaded.
  Fixes #11831.
  [smcmahon]

4.1rc1 - 2011-05-20
-------------------

- Make folder_listing filter on @@portal_state/friendly_types when applied to
  a container. (Add portal_types to site_properties types_not_to_list to
  exclude them from friendly_types.)
  [elro]

- Error handling for folder_full_view_item so items using a BrowserView render
  a link instead of causing an error.
  [elro]

- Refactor dragdropreorder.js and folder_moveitem to detect client/server
  ordering mismatches and be more robust in event of mousing out of the table
  rows.
  [elro]

- Add forward compatibility with DateTime 3.
  [hannosch]

- Added a new interface blacklist to the `CatalogTool` module. Items in this
  list won't be indexed in the object_provides index. This saves about 1kb of
  mostly useless data to be stored per object. If you need to query on one of
  the blacklisted interfaces, consider using other indexes to get a small
  result set and then checking the actual objects or add a specialized index
  for the data you are interested in. Also changed the stored value to a tuple
  to safe some memory overhead of the list type.
  [hannosch]

- Optimize images and icon file sizes.
  [hannosch]

- Fix the event_view to refer to the `icon_export_*` images relative to the
  portal and not the current context.
  [hannosch]

- Text on login success page uses navigation root title instead of portal title.
  Refs http://dev.plone.org/plone/ticket/9175.
  [thomasdesvenain]

- Let the content import step (importing the site structure) not
  depend on plone-final but on typeinfo.  Solves circular dependency.
  Refs http://dev.plone.org/plone/ticket/8350
  [maurits]

- Set Content-Language header to default language when content language is an
  empty string.
  [elro]

- Change csrf patch to apply to MemberAdapter instead of MemberData when using
  CMF 2.3.
  [elro]

- CMFCore registers a memberdata export/import handler in 2.3, so make our
  registration conditional.
  [elro]

- Remove `previous` sub-collection from default content, as sub-collections are
  not enabled by default since Plone 4.0 and having one in the default content
  is confusing. Closes http://dev.plone.org/plone/ticket/10705.
  [hannosch]

- Fix zope.sendmail patch to raise errors for immediate sending failures.
  Relates to http://dev.plone.org/plone/ticket/10675.
  [elro]

- Sort on content title ignores accents.
  So, d < é < f.
  [thomasdesvenain]

- Expose the query report and plan on the catalog tool.
  [hannosch]

- Optimize the data indexed by the `allowedRolesAndUsers` index and the query
  performed against it.
  [hannosch]

- Fix circular dependency in import steps.
  This partially fixes http://dev.plone.org/plone/ticket/8350
  [kiorky]

4.1b2 - 2011-04-06
------------------

- Fix bug in formUnload.js where changes to select option lists without a
  default were incorrectly detected (javascript indexes from 0, not 1.)
  [elro]

- Added "rss" alias to "RSS".
  This fixes https://dev.plone.org/plone/ticket/11638.
  [gotcha]

- Fixed: "showing field with error is broken in edit view"
  This fixes https://dev.plone.org/plone/ticket/11686.
  [gotcha]

- Fixed: "missing required icon in tabs in edit view"
  This fixes https://dev.plone.org/plone/ticket/11685.
  [gotcha]

- Make wicked an optional dependency. (It is still pulled in by the Plone
  distribution.)
  [davisagli]

- Fix import of RoleManager to avoid deprecation warning.
  [davisagli]

- Update MigrationTool.getSoftwareVersion to return Products.CMFPlone version.
  [elro]

4.1b1 - 2011-03-06
------------------

- Remove useless trailing slash in 404.
  This fixes http://dev.plone.org/plone/ticket/11550
  [gotcha]

- Remove invocation of do_search_collapse from advanced search form.
  It caused the function to run twice, making collapsibles wink
  rather than open. Fixes http://dev.plone.org/plone/ticket/11565
  [smcmahon]

- Use correct argument order in utranslate.py script.
  This fixes http://dev.plone.org/plone/ticket/10395
  [fRiSi]

- Add missing security declarations on PropertiesTool.
  [davisagli]

4.1a3 - 2011-02-14
------------------

- Discontinue tagging plone_3rd party as a separate external.
  [esteele]

4.1a2 - 2011-02-10
------------------

- On search form don't show list of users when anonymous
  unless explicitly allowed in @@security-controlpanel.
  Fixes http://dev.plone.org/plone/ticket/11346
  [msmith64]

- Add fallback icon for control panels with no icon, in the portlet_prefs
  portlet. This fixes http://dev.plone.org/plone/tickets/11112.
  [topherh, davisagli]

- Use the new optimized BooleanIndex for the `is_default_page` and
  `is_folderish` indexes and the new `UUIDIndex` for the `UID` index.
  [hannosch]

- Remove js-generated inline style from searchbox. Same CSS is in public.css.
  Fixes http://dev.plone.org/plone/tickets/11186.
  [msmith64]

- Use nocall: when getting the @@sitemap_view in sitemap.pt.
  [elro]

- Hide plone.app.registry, z3c.form as an add-on options from the
  @@plone-addsite view, quickinstaller.
  [esteele]

- Merge in PLIP #9288: Improved commenting infrastructure. Refs
  http://dev.plone.org/plone/ticket/9288
  [timo]

- Fixed handling of relative links used as default pages
  http://dev.plone.org/plone/ticket/11340
  [fRiSi]

4.1a1 - 2011-01-18
------------------

- Removing unused import from testCatalogTool.
  [thet]

- Alphabetical ordering of metadata.xml dependencies.
  [thet]

- Using tom gross' improved and tested safeToInt version.
  [tom_gross, thet]

- Move PlacefulWorkflow, kupu, iterate and openid to Plone egg dependencies.
  [elro]

- Depend on plone.app.uuid for indexing content UUIDs.
  [toutpt, davisagli]

- Added ++resource++blank.html, a building block for cross-domain iframe
  communication (e.g. with Disqus.)
  [elro]

- Added iframe option for single sign on login templates.
  [elro]

- Removed duplicate code in login templates.
  [elro]

- Added ajax_include_head request parameter for use with cross domain iframe.
  [elro]

- Single Sign On support in login forms.
  [elro]

- Refactored ``URLTool.isURLInPortal``, adding ``allow_external_login_sites``
  property to ``site_properties`` for external sites considered to be internal
  for the purposes of logging in.
  [elro]

- Improve table sort of 'listing' class tables. We can use a sortabledata-xxxx
  class in a cell (td) where xxxx is a sortable data value, then, sort uses xxxx
  value to compare cell values, instead of td text content.
  Refs http://dev.plone.org/plone/ticket10809
  [thomasdesvenain]

- Merge in PLIP #10901: Set and enforce base coding standards for our own
  JavaScript. Refs http://dev.plone.org/plone/ticket/10901
  [esteele]

- Removed IOrderedContainer-implementation from PloneFolder in favour
  of implementation in OFS.OrderSupport
  [tom_gross]

- Renamed package to `Products.CMFPlone`.
  [elro]

- Deprecated the following scripts that are only used by deprecated templates.
  These will be removed in Plone 5: prefs_group_edit.py,
  prefs_valid_search_restriction.py, prefs_user_group_search.py,
  prefs_portrait_delete.py.
  [davisagli]

- Replaced the prefs_group_details.pt template with a browser view in
  plone.app.controlpanel. Ss a side effect this means group creation is now
  protected by the Plone Users and Groups control panel permission, rather than
  the CMF Manage Groups permission.
  [davisagli]

- Turn plone_control_panel.pt into a deprecated alias for the
  @@overview-controlpanel view from plone.app.controlpanel.
  [davisagli]

- Protect most control panels with specific permissions instead of the generic
  "Manage portal".
  [davisagli]

- Configure the Site Administrator role in the default rolemap and workflows.
  This role is intended for people who should have full content editing
  privileges but not Manager access (i.e. to the ZMI).
  [davisagli]

- Updated to use Zope 2.13.
  [hannosch]


4.0.9 - 2011-07-19
------------------

- Release Plone 4.0.9
  [esteele]

4.0.8 - 2011-07-05
------------------

- Use ``transaction.savepoint`` instead of ``transaction.begin`` in
  ``isLinked``;
  closes #7784;
  does not reopen #6666 probably because we use fixed version of ZEO
  [gotcha]

- Optimized: Huge optimization of calendar_formfield.js under ie8 and lower.
  Gain of 50% on js execution on a large page.
  [thomasdesvenain]


4.0.7 - 2011-06-02
------------------

- Apply patches to prevent exploitation of CVE-2011-1948 (Hotfix 20110531.)
  [elro]

- Set Language to 'all' to list content in all languages when listing a
  worklist's contents (workflow) to support LinguaPlone better.
  [mj]

4.0.6 - 2011-05-20
------------------

- Backport set appropriate cache headers on createObject redirects to prevent
  caching by proxy servers.
  [elro]

- Fix form tab navigation when it has more than 6 tabs under ie, chrome, safari.
  This fixes http://dev.plone.org/plone/ticket/11815.
  [thomasdesvenain]

- Let the content import step (importing the site structure) not
  depend on plone-final but on typeinfo.  Solves circular dependency.
  Refs http://dev.plone.org/plone/ticket/8350
  [maurits]

- Backport fix zope.sendmail patch to raise errors for immediate sending
  failures. Relates to http://dev.plone.org/plone/ticket/10675.
  [elro]

- Fix form submission when it has more than 5 tabs.
  This fixes http://dev.plone.org/plone/ticket/10868.
  [thomasdesvenain]

- Fix circular dependency in import steps.
  This partially fixes http://dev.plone.org/plone/ticket/8350
  [kiorky]

4.0.5 - 2011-04-06
------------------

- Fixed: "showing field with error is broken in edit view"
  This fixes http://dev.plone.orgplone/ticket/11686.
  [gotcha]

- Fixed: "missing required icon in tabs in edit view"
  This fixes http://dev.plone.orgplone/ticket/11685.
  [gotcha]

- Added "rss" alias to "RSS".
  This fixes http://dev.plone.orgplone/ticket/11638.
  [gotcha]

- Fixed: "Show all" livesearch link manages "current folder only" option.
  This fixes http://dev.plone.orgplone/ticket/11414.
  [thomasdesvenain]

- Fixed: "Show all" was not displayed in live search
  when limit result was exceeded.
  This fixes http://dev.plone.orgplone/ticket/11628.
  [thomasdesvenain]

4.0.4 - 2011-02-26
------------------

- Fixed: "Show all" livesearch link manages "current folder only" option.
  This fixes http://dev.plone.orgplone/ticket/11414.
  [thomasdesvenain]

- Fixed: "Show all" was not displayed in live search
  when limit result was exceeded.
  This fixes http://dev.plone.orgplone/ticket/11628.
  [thomasdesvenain]

- Add fallback icon for control panels with no icon, in the portlet_prefs
  portlet. This fixes http://dev.plone.org/plone/tickets/11112.
  [topherh, davisagli]

- Remove js-generated inline style from searchbox. Same CSS is in public.css.
  See http://dev.plone.org/plone/changeset/40654,
  Fixes http://dev.plone.org/plone/ticket/11186
  [msmith64]

- Fixed handling of relative links used as default pages.
  This fixes http://dev.plone.orgplone/ticket/11340.
  [fRiSi]

- Re-instate spinner.gif (animation), lost in the move to PNGs. The static
  spinner.png has been deprecated.
  Fixes http://dev.plone.org/plone/ticket/11504.
  [mj]

4.0.3 - 2011-01-18
------------------

- Change PloneBatch class to work with actual_result_count alone instead of
  calculating the length of the provided sequence.
  [hannosch]

- Pass on batching hints to the catalog query in `getFolderContents`.
  [hannosch]

- Make role/permission settings consistent in Plone root
  http://dev.plone.org/plone/ticket/7922
  [tom_gross]

- Added some css ids on login form.
  [thomasdesvenain]

- Fixed possible Unauthorized error when registering a user when using
  the email address as login name.
  [maurits]

- Fixed errors on kss update in portal factory.
  This fixes http://dev.plone.org/plone/ticket/11311.
  [thomasdesvenain]

- In the registration tool strip the mail text before passing it
  through message_from_string.  A leading white line would prevent
  getting Subject, To and From headers from the generated message.
  [maurits]

- Avoid various deprecation warnings under Zope 2.13.
  [hannosch]

4.0.2 - 2010-11-15
------------------

- Added fill-slot to events_listing.pt that was not showing any events.
  This fixes http://dev.plone.org/plone/ticket/11216.
  [jmansilla, WouterVH]

- Fixed ``factory.addPloneSite`` so extension profiles have a chance of
  specifying site properties in a ``properties.xml`` file.
  [hannosch]

- Edit tab on Author page pointed to personal preferences page instead of
  personal information.
  This fixes http://dev.plone.org/plone/ticket/11141.
  [piv]

- Fixed http://dev.plone.org/plone/ticket/11160,
  first level of Table of Contents is a level with at least two entries.
  [thomasdesvenain]

- Fixed: http://dev.plone.org/plone/ticket/11177, some formselector
  specifications for popups were too vague.
  [smcmahon]

- Fixed: http://dev.plone.org/plone/ticket/11187, Better message when
  you cannot delete a locked item
  [kiorky]

4.0.1 - 2010-09-28
-------------------

- Fixed : 'listing' class table sort of first column failed (at third click).
  [thomasdesvenain]

- Re-add suggestions for 404 pages that were missing in 4.0.
  [MatthewWilkes]

- Block picking a username already in use by a parent PAS to prevent potential
  security issues due to collisions.
  [MatthewWilkes]

- Successful completion of contact form ended in redirect to 'undefined'
  when using popups. Fixed by just closing.
  Fixes http://dev.plone.org/plone/ticket/11090
  [smcmahon]

- Fixed i18n of the Upgrade hellip button in plone-overview.pt.
  [vincentfretin]

- Fix a malformed list comprehension in failsafe_login_form.cpt
  [esteele]

- Modified plone.css.py script to correctly show contents for z3 style resources, by
  using portal_css.getInlineResource.
  This fixes http://dev.plone.org/plone/ticket/10864
  [mr_savage]

- Fixed http://dev.plone.org/plone/ticket/10956 - prevent content of the
  types listed in typesUseViewActionInListings from being selected as default
  pages.
  [elro]

- Validate new group names using the isMemberIdAllowed method of the
  registration tool. This fixes http://dev.plone.org/plone/ticket/10897.
  [davisagli]

- Add a default icon when there is no icon defined in a configlet.
  This prevent broken images on IE. This fixes http://dev.plone.org/plone/ticket/11112.
  [kiorky]

4.0 - 2010-08-28
----------------

- Tag 4.0 final.
  [esteele]

4.0rc1 - 2010-08-05
-------------------

- Fixed http://dev.plone.org/plone/ticket/10790
  "popupforms.js causes javascript error on IE7"
  [smcmahon]

- Limit number of matches looked up during live search for speedier replies.
  [witsch]

- Use the standard libraries doctest module.
  [hannosch]

- Don't open content_status_history in a popup, it requires template specific
  JS and CSS to be loaded. This refs http://dev.plone.org/plone/ticket/10726.
  [hannosch]

- No longer mention `textile` as a supported markup style. We don't ship with
  the required Python packages by default. This closes
  http://dev.plone.org/plone/ticket/10690.
  [hannosch]

- Fix the table of contents generation script to include h1 tags from the
  content body. Fixes http://dev.plone.org/plone/ticket/10755
  [davisagli]

- Update `plone-upgrade.pt` to explicitly check if a Plone instance has
  been downgraded since the database was created. This fixes:
  http://dev.plone.org/plone/ticket/10220
  Thanks to davidblewett for the patch.
  [claytron, davisagli]

- Update license to GPL version 2 only.
  [hannosch]

- Use Unicode characters instead of HTML entities in the default front page
  text. This closes http://dev.plone.org/plone/ticket/10084.
  [hannosch]

- Replace the `manage_zmi_logout` link and page with a nicer Plone specific
  implementation.
  [hannosch]

- Fixed the visual appearance of the `logged_out` page.
  [hannosch]

- Stop issuing deprecation warnings about action icons in our default install.
  [hannosch]

- Silence the ISO8601 warning until we fixed all of Plone Core. This refs
  http://dev.plone.org/plone/ticket/10322.
  [hannosch]

- Avoid deprecation warning in sendmail patch and require at least Zope 2.12.9.
  [hannosch]

- Removed long unused ``ie5fixes.js``. This refs
  http://dev.plone.org/plone/ticket/10287.
  [hannosch]

- Be a bit less noisy in GenericSetup handlers and don't log a
  ``Nothing to import`` message for our own handlers.
  [hannosch]

- Fix broken userid/login name in the password reset code. Fixes
  http://dev.plone.org/plone/ticket/10767
  [wichert]

4.0b5 - 2010-07-07
------------------

- Don't show the site's logo on the upgrade screen. Trying to render it can
  cause problems on not yet upgraded sites.
  [hannosch]

- No longer show relevance percentage numbers in search results. What matters
  to users is the search results order; the numbers are meaningless.
  [hannosch]

- No longer include a searchterm parameter in the query string when linking
  from the search results page, as it will be picked up from the referer.
  [davisagli]

- Fix the highlightsearchterms script to not apply highlighting within
  textareas, to avoid data loss. Fixes http://dev.plone.org/plone/ticket/10573
  [davisagli]

- Improved comment display and behavior: Now opens "Add comment" in an
  overlay, no longer insists on a Subject for every comment, and more readable
  layout. Also improved the error messages.
  [limi]

- Switching the default modal window effect to be a white-out instead of a
  darkened effect. With large windows, the darkening is very distracting, and
  it also reminds people of the UAC prompts from Windows Vista/7, which is not
  a good thing. ;)
  [limi]

- Removing action links from Events, since they are in the template (and were
  never supposed to have actions in the first place). This fixes
  http://dev.plone.org/plone/ticket/10540.
  [limi]

- Better icon for the theme control panel. (Thanks, Tango!)
  [limi]

- Added normalizeString to the Plone view interface, where the declaration was
  missing.
  [davisagli]

- Add a contenttype class to the items listed in select_default_page.cpt, so
  they can get sprited icons. Fixes http://dev.plone.org/plone/ticket/10577.
  [davisagli]

- Add a contenttype class to the links in the livesearch results, so that
  they can get sprited icons. Fixes http://dev.plone.org/plone/ticket/10512.
  [davisagli]

- Avoid using the deprecated five:implements directive.
  [hannosch]

- Avoid testing dependency on zope.app.testing.
  [hannosch]

- No longer use the extra argument to the functional tests publish method.
  [hannosch]

- Make the jQueryTools overlay configuration options in popupforms.js be
  the default overlay configuration for jQueryTools so that popup forms in
  other add-ons look similar.
  [smcmahon]

4.0b4 - 2010-06-03
------------------

- Fix FactoryTool to mangle REQUEST.BASEn correctly.
  [elro]

- Updated the description_user_management default message in
  plone_deprecated/prefs_users_overview.cpt to be the same as
  plone/app/controlpanel/usergroups_usersoverview.pt
  [vincentfretin]

- Ensure text is shown for the various Collection views. This fixes
  http://dev.plone.org/plone/ticket/10226
  [pelle]

- Set the correct meta_type for files and images.
  [hannosch]

- Removed the Large Plone Folder portal_type and LargePloneFolder class.
  Instead, use a normal ATFolder from plone.app.folder, with its ``ordering``
  attribute set to u'unordered'. Existing Large Plone Folders will get
  migrated when upgrading from older versions of Plone.
  [davisagli]

- Removed empty HTML tags from listings when an item in the listing has no
  description.
  [spliter]

- Fix bad test for valid paste data in object_paste.
  [wichert]

- Remove deprecated IndexIterator class and tabindex html attribute
  [edegoute]

- Use a mask to visually highlight modal overlays. Configurable in
  popupforms.js. Set a common set of configuration options, defaulting
  to overlays that use absolute positioning.
  [smcmahon]

- Update the ZMI security tab warning so it doesn't display outside of a Plone
  site.  This fixes http://dev.plone.org/plone/ticket/10521.
  [davisagli]

- Get configlet icons directly from the action, rather than using the
  getIconFor helper.  This breaks the backwards-compatible fallback to the
  action icons tool, but avoids re-evaluating all action conditions for each
  configlet.
  [davisagli]

- Report expiration of password resets for registration as an absolute time,
  rather than a number of hours.
  [davisagli]

4.0b3 - 2010-05-03
------------------

- "(Requires Javascript)" is now translatable in accessibility-info.pt.
  This closes http://dev.plone.org/plone/ticket/10475
  [vincentfretin]

- Revert changes from changeset 34269, which prevented the calendar widget
  from properly saving results. Add another hidden field for the purposes
  of handling the label's for attribute.
  Fixes http://dev.plone.org/plone/ticket/10450
  [esteele]

- Update capitalization of i18n:translate-d tags in deprecated templates to
  avoid i18ndude warnings on new templates.
  [esteele]

- Updated default_error_message.pt to provide a better 404 Error page as per
  http://dev.plone.org/plone/ticket/8667
  [cwainwright, dunlapm]

- Fixed newsitem_view to not render the caption if the field is empty.
  [limi]

- Moved old GIF variants of the icons to plone_deprecated, since Plone itself
  uses the PNG variants now.
  [limi]

- Added touch_icon.png for iPhone/iPad home screen support.
  [limi]

- Fixed clipped icons for most of the content type sprites by centralizing the
  definitions and setting line-height to 2em. There's still an issue where
  tal:replace="structure item_icon/html_tag" renders an img tag without src or
  points to the root, which makes the layout have an empty element. Probably
  needs to be fixed in the html_tag expression (e.g. if there isn't anything
  there, don't render). Should be good enough for beta3, but needs to be fixed
  before RC. See LiveSearch results + Advanced Workflow + Collection view
  (e.g. "Events") for examples of this. References
  http://dev.plone.org/plone/ticket/10409,
  http://dev.plone.org/plone/ticket/10466
  [limi]

- Don't take values directly from the request in ``getFolderContents``.
  request.form can include arbitrary data and request.other contains a whole
  lot of data, which isn't valid catalog indexes.
  [hannosch]

- Don't send Bcc header with Mailhost.secureSend. Renamed CC header to Cc.
  [vincentfretin]

- Fixed folder_listing.pt so it doesn't stringify and then reparse the start
  and end dates of events (this also fixes a timezone issue,
  http://dev.plone.org/plone/ticket/10445)
  [davisagli]

- Fixed folder_listing.pt so that it shows event dates in a cleaner way
  (no more redundant listing of times + dates when and event is on one day
  has same start + end time)
  [jonstahl]

- Change the title of the Users folder to be more in line with its actual
  function.
  Fixes: http://dev.plone.org/plone/ticket/9693
  [cwainwright]

- Inject contentFilter as `**kw` params to topic's queryCatalog and not as first
  argument which should be the REQUEST, if given. With that in place, batching
  on contentFiltered topics works again.
  Fixes: http://dev.plone.org/plone/ticket/10428
  [thet]

- Template for editing user preferences (prefs_user_details) is replaced by
  personal information and preferences forms from plone.app.users. Moved
  prefs_user_details and prefs_user_edit to deprecated skins.
  http://dev.plone.org/plone/ticket/10327
  [kcleong]

4.0b2 - 2010-03-09
------------------

- Explicitly check that a searchterm was provided before adding it to the
  query string.
  Fixes http://dev.plone.org/plone/ticket/9025
  (Port of [35909])
  [blueaidan]

- Batch folderContents in folder_listing's listing macro if it's not already
  batched when passed in. This closes http://dev.plone.org/plone/ticket/10401
  [davisagli]

- Added overlays for Rename and selecting default folder views.
  [limi]

- Made the core content types use CSS sprites instead of individual images,
  which cuts down the number of image HTTP requests from 11 to 2.
  This fixes http://dev.plone.org/plone/ticket/10403
  [limi]

- Cleaned up the type descriptions, and removed the ones where that are
  self-evident or redundant.
  [limi]

- Fix several issues in the RSS template: don't get the logo name from
  base_properties, correctly fetch the full text and last modified date, and
  only specify the publishing date in the output.
  [davisagli]

- Add and adapt tests for moving dates bug which was caused by date
  conversion without respect to Daylight Saving Times.
  Fix for http://dev.plone.org/plone/ticket/10141
  [thet]

- Removed msgid for "Site Setup" message in portlet_prefs.pt
  and plone_control_panel.pt.
  [vincentfretin]

- Added in support WebKit- and Gecko-based small-screen devices
  (iPhone, Android, Firefox Mobile)
  [limi]

- Make prefs_main_template fill portlets_one_slot instead of column_one_slot
  to add its portlet, for compatibility with Sunburst.  Also make it
  unnecessary for custom configlet templates to set display_border.
  [davisagli]

- Adjusted viewlet configuration so that the Sunburst theme uses the viewlets
  defined in plone.app.layout, and the Classic theme overrides that
  configuration to achieve the old viewlet positions.
  [davisagli]

- batch_macros.pt: Use request/ACTUAL_URL instead of context/absolute_url as
  batching base url so that batching works for different views and FSPageTemplates
  appended to context/absolute_url.
  The approach ${context/absolute_url}/${template/getId} didn't work for views.
  [thet]

- Fix columns in prefs_main_template.
  [davisagli]

- Use zope.app.locales >= 3.6.0, this package have now a configure.zcml
  which register the translations, we use it now.
  A new version of zope.app.locales is needed to fix
  http://dev.plone.org/plone/ticket/10105
  [vincentfretin]

- Fix argument order in translate Python script.
  [davisagli]

- Simplify folder_tabular_view to use the folder_listing macros.
  [elro]

- folder_listing should batch for collections, like folder_tabular_view.
  This was introduced to fix #7937 but it no longer seems to be a problem.
  [elro]

- Simplified the "Event when" i18n introduced in 4.0b1.
  [vincentfretin]

- Fixed DYNAMIC_CONTENT in heading_prefs_user_details message.
  [vincentfretin]

- Updated the table_sorter.js to use Unicode for its arrows instead of images.
  Also made it more robust, so it doesn't fail if you have two columns with
  the same name. This refs http://dev.plone.org/plone/ticket/10352
  [davisagli, limi]

- Stop removing the $ alias for jQuery, since many plugins rely on it. Users
  worried about conflicts with other libraries can customize
  jquery-integration.js and set jq = jQuery.noConflict() again, instead of
  jq = jQuery
  [davisagli, limi]

- For Managers, make default_error_message display tracebacks inline rather
  than linking to them.
  [davisagli, limi]

- Fixed livesearch_reply.py to give the context to ts.translate method.
  [vincentfretin]

- Fixed plone_scripts/translate.py to use translation_service.translate
  method. translation_service.utranslate was removed in recent version of
  PlacelessTranslationService.
  [vincentfretin]

- Reverted default message for description_group_members_of in
  plone_deprecated/prefs_group_members.cpt
  [vincentfretin]

- Fixed help_biography message.
  [vincentfretin]

- Internationalized the backup-warning message in plone-upgrade.pt.
  [vincentfretin]

- Removed template_id from batch_base_url in batch_macros.pt because it breaks
  when overloading the folder_listing template via zcml.
  [thet]

- Convert limit_display to int in folder_tabular_view.pt and folder_listing.pt
  so that it can be fed in via request parameters.
  [thet]

4.0b1 - 2010-03-08
------------------

- "Event when" improved for better i18n.
  This closes http://dev.plone.org/plone/ticket/10196
  [gotcha]

- Adjust the tests now that `DateTime` objects are stored with a time zone.
  Refs http://dev.plone.org/plone/ticket/10141
  [witsch]

- Fix issues with sliding modification/publishing dates by using `DateTime`'s
  `ISO8601` method instead of `ISO`, which doesn't include time zones.
  Refs http://dev.plone.org/plone/ticket/10140, 10141 & 10171.
  [davisagli, witsch]

- Set the 'context' context on Plone expression contexts, which is needed for
  resolving UnicodeDecodeErrors when evaluating expressions.
  [davisagli]

- Added optional batchformkeys parameter to batch_macros.pt to restrict which
  form fields will be included in batch navigation links (for immediate use
  in plone.app.controlpanel's user and groups listsings).
  [cah190]

- Added markup to give styling to document ByLine in folder_summary_view.
  This fixes http://dev.plone.org/plone/ticket/6094
  [dunlapm]

- Add an HTML id to the "add group" form.
  [stuttle]

- Moved the tal:condition from the <img> tag to <a> tag in folder_summary_view,
  to remove unnecessary empty <a> tags when no image exists.
  References http://dev.plone.org/plone/ticket/10251
  [miguelitosm]

- Removed the 'ListFolderContents' permission from all workflows and limit the
  default permission to Manager, Owner, Reviewer, Editor and Contributor.
  It should not change with workflow state, it's an edit/admin view that you
  either should have or not.
  References http://dev.plone.org/plone/ticket/10236
  [tomster]

- Switched plone.kss from relying on redundant #region-content to #content.
  References http://dev.plone.org/plone/ticket/#10231
  [spliter]

- Hide the Kupu and placeful workflow add-ons at normal site creation time.
  [hannosch]

- Ensure that implicitly selected profiles are installed first, so themes
  depending on them are installed correctly. This closes
  http://dev.plone.org/plone/ticket/10223.
  [hannosch]

- Cleaned plone_control_panel.pt and fixed it's validation.
  [spliter]

- Moved portalStatusMessage in author.pt above #content for case when the
  user is not found. References
  http://dev.plone.org/plone/ticket/10231
  http://dev.plone.org/plone/ticket/9981
  [spliter]

- Upgraded to jQuery 1.4.2.
  [mj]

4.0a5 - 2010-02-19
------------------

- Replace `getObjPositionInParent` with stub index capable of sorting search
  results according to their position in the container, a.k.a. "nogopip".
  [witsch]

- Move `isExpiry` into `CMFPlone.utils` so it can be called directly,
  i.e. without searching the skin.
  [witsch]

- Removed redundant 'configlet' class from prefs_group_details.pt and
  prefs_user_details.pt
  [spliter]

- Updated more prefs_* templates to follow recent markup conventions.
  References http://dev.plone.org/old/plone/ticket/9981
  [spliter]

- Removed deprecated 'sub' slot from discussionitem_view.pt.
  [spliter]

- Added a condition to the automatic loading of ZCML configuration (via the
  ``[z3c.autoinclude.plugin]`` ``target = plone`` entry point), so that it
  is possible to disable automatic loading. This is particularly useful in
  tests, where automatically included packages can cause leakage of state or
  unrelated errors if Plone's ZCML is loaded. To disable auto-inclusion,
  you can add a ZCML statement like the following::

    <configure xmlns="http://namespaces.zope.org/zope"
               xmlns:meta="http://namespaces.zope.org/meta">
        <meta:provides feature="no-autoinclude" />
    </configure>

  You need to do this "early", i.e. before Plone's ZCML is loaded.
  [optilude]

- Fix a test regression in discussion_reply_form if the layout for the
  item being discussed has no content-core macro.  (Such as the
  link_redirect_view.py script for a Link item).
  [davisagli]

- Wrapped .contentViews and .contentActions with <div id="edit-bar"> in views.
  [spliter]

- Wrapped .contentViews and .contentActions with <div id="edit-bar"> in order
  to have consistent markup between classic and Sunburst themes.
  [spliter]

- Cleaned up some markup mess, #region-content, .documentContent were redundant,
  and were reduced to #content instead, to reduce confusion.
  Full explanation here: http://dev.plone.org/plone/ticket/10231, and
  instructions for theme authors here:
  http://plone.org/documentation/kb/how-to-write-templates-for-plone-4
  [limi]

- Moved the prepareObjectTabs method from the @@plone view to the
  ``plone.contentviews`` viewlet.
  [hannosch]

- Moved layout related methods from the @@plone view to a new @@plone_layout
  view found in plone.app.layout.globals.
  [hannosch]

- Add a `meta:provides` directive to `meta.zcml` that provides the feature
  `plone-4`. To load Plone-4 specific ZCML, you can use something like this::

    <configure xmlns="http://namespaces.zope.org/zope"
               xmlns:zcml="http://namespaces.zope.org/zcml">
        <include zcml:condition="have plone-4"
                 file="plone-4-specific-stuff.zcml" />
    </configure>

  [optilude]

- Add new editing control panel.
  [hannosch]

- Hide the rss and print document actions for new sites. Both are consistently
  supported by browsers today and don't need site specific actions anymore.
  [hannosch]

- We need to include ZCML from `plone.app.folder`, not just `plone.folder`.
  This refs http://dev.plone.org/plone/ticket/10127.
  [witsch, hannosch]

- Removed the no longer needed history viewlet. This refs
  http://dev.plone.org/plone/ticket/10102.
  [hannosch]

- Made history act as an ajax popup rather than an inline collapsible. The
  goal is to reduce rendering time when history isn't needed.
  [smcmahon]

- Updated author.pt to follow general markup conventions.
  References http://dev.plone.org/plone/ticket/9981
  [spliter]

- Updated templates to fill 'main' slot with <metal:main fill-slot='main'>
  construction instead of <div metal:fill-slot="main" tal:omit-tag="">
  [spliter]

- Re-factored plone_prefs/ templates to follow the recent markup conventions.
  References http://dev.plone.org/plone/ticket/9981
  [spliter]

- Added 'All content' blog like view for folderish types.
  [elro]

- Re-factored folder listing and summary view.
  [elro]

- Updated templates to disable the columns with 'disable_MANAGER_NAME'
  pattern.
  [spliter]

- Add current portal type to the body css class like the section
  and template css class's.
  Refs http://dev.plone.org/plone/ticket/8777.
  [pelle]

- Deprecate the portlets_fetcher and macro_renderer templates.
  [davisagli]

- Clean up various HTML comments that were being emitted unnecessarily.
  [davisagli]

- On the Zope overview screen, make sure the user is authenticated at
  the Zope root before sending them to the upgrade view for a Plone
  site, when the Upgrade button is clicked.  This closes
  http://dev.plone.org/plone/ticket/10154.
  [davisagli]

- Increased maximum length of the sortable_title index from 40 to 70 characters
  to match truncation rules of most search engines. This closes
  http://dev.plone.org/plone/ticket/10170.
  [hannosch]

- Restrict manage_options on the catalog to supported and useful options.
  [hannosch]

- Re-factored all templates to follow the recent markup conventions.
  References http://dev.plone.org/plone/ticket/9981
  [spliter]

- Register common CSS resources as blank files here. Other themes are
  supposed to override them to style the site appropriately.
  Refs http://dev.plone.org/plone/ticket/9988.
  [dukebody]

- Updated markup for kss_generic_macros and made main_template to use that
  as the default generator for titles and descriptions.
  [spliter]

- Cache the Plone expression context in the _plone_ec_cache attribute of the
  request, rather than _ec_cache, to avoid accidentally getting a plain CMF
  expression context if that's the first sort that was fetched.
  [davisagli]

- Update profile version, so we can register new upgrade steps.
  [hannosch]

- Fix portal_factory to not destroy sub-path traversal. For example, a view
  that implements IPublishTraverse would previously not see the traversal
  sub-path if invoked on an item being edited in the portal_factory.
  [optilude]

4.0a4 - 2010-02-01
------------------

- Define a "content-core" macro for each content view template to make blog
  like listings possible.
  [elro]

- Make sure the default content folders (news, events, and Members) are
  not explicitly ordered (e.g., equivalent to the old Large Plone Folder
  type).
  [davisagli]

- Show user's fullname in form header in prefs_user_details
  [esteele]

- Deprecated plone_prefs/prefs_search_macros.pt
  [esteele]

- Deprecated plone_prefs/prefs_user_memberships.pt,
  plone_prefs/prefs_user_memberships.pt.metadata,
  plone_prefs/prefs_user_membership_edit.py,
  plone_prefs/prefs_user_group_search.py. Functionality is now handled by
  @@usergroup-usermembership.
  [esteele]

- Overlay form on @@usergroup-groupprefs and @@usergroup-userprefs now
  redirects to the current page instead of reloading it. Reloading caused a
  resubmission of the last form action (such as "delete") which threw an
  error.
  [esteele]

- Deprecated plone_deprecated/prefs_group_members.cpt,
  prefs_group_members.cpt.metadata, prefs_group_members_add.cpy,
  prefs_group_members_add.cpy.metadata, prefs_group_members_delete.cpy,
  prefs_group_members_delete.cpy.metadata. These are now handled by
  @@usergroup-groupmembership in plone.app.controlpanel
  [esteele]

- In the tests, patch the MockMailHost to give it a secureSend method,
  just like we already patch the real MailHost.
  [maurits]

- Make QuickInstallerTool.upgradeProduct() able to handle upgradeSteps
  directive.
  Closes http://dev.plone.org/plone/ticket/9455
  [cah190]

- Update jquery.js to use jquery-1.4.min.js. The change is in
  Plone3rdParty/branches/4.0/skins/plone_3rdParty
  [smcmahon]

- Remove explicit iefixes (css and js) from the main_template, which
  will be pulled now from the ResourceRegistries, using the
  conditionalcomments property.
  Refs http://dev.plone.org/plone/ticket/9278.
  [dukebody]

- Move iefixes.js to the ploneclassic.theme package, since we agreed
  upon that every theme should be responsible of its own fixes for IE.
  Refs http://dev.plone.org/plone/ticket/9278.
  [dukebody]

- Make global_cache_settings responsible for deciding to switch on gzip
  compression instead of doing it in the enableHTTPCompression script. This
  avoids another costly Python script call.
  [hannosch]

- Avoid the test function in the main_template. It doesn't exist in view page
  template files.
  [hannosch]

- Avoid the getSectionFromURL method completely and merge functionality into
  the bodyClass method.
  [hannosch]

- Display logoIcon.png instead of favicon.ico on the Zope root overview screen,
  for compatibility with IE which refuses to render X-ICON format images in the
  document body.
  [davisagli]

- Avoid yet another mindless Python script and deprecate renderBase.
  [hannosch]

- Simplify the charset handling, by moving the actual setting into the
  global_cache_headers macro.
  [hannosch]

- Replaced the getSectionFromURL Python script with a view method.
  [hannosch]

- Deprecated the computeRelatedItems script in favor of a method on the
  related items viewlet.
  [hannosch]

- Hide plonetheme.classic from the list of uninstallable products to reduce
  confusion, as at this point it can't be uninstalled without breaking
  sunburst as well when the Quick Installer unregisters its CSS.
  [davisagli]

- Altered table of contents javascript so that comments are not displayed.
  Refs. #8621.
  [dbfrombrc]

- Added back INavigationRoot to CMFPlone.browsers. We need to provide an
  upgrade step for persistent marker interfaces before removing it.
  This refs http://dev.plone.org/plone/ticket/10072.
  [hannosch]

- Updated markup of document_view and event_view to follow conventions
  in main_template.
  References http://dev.plone.org/plone/ticket/9981
  [spliter]

- Just a markup polishing - <metal> tags don't need explicit "metal" for
  defining slots.
  [spliter]

- plone.belowcontent should not replace div#viewlet-below-content but
  rather add content into it
  [spliter]

- Moves plone.abovecontent and plone.belowcontent viewlet managers actually
  above and below content respectively.
  Closes http://dev.plone.org/plone/ticket/10081
  [spliter]

- Put the preferred markup for content area in main_template. References #9981
  [spliter]

- Remove prefs_group_modify.cpy as we no longer use it. Adjust tests accordingly.
  [esteele]

- Rework the prefs_group_details form to properly redirect back to the new
  @@usergroup-groupprefs page when creating a new groups, and postback to
  itself when modifying existing groups.
  [esteele]

- Add popup for add group form.
  [smcmahon]

- Pass group title and description through to the editGroups request, to
  ensure the those properties on the groups are updated. Allows the display of
  titles in @@usergroup-groupprefs
  Closes http://dev.plone.org/plone/ticket/7277
  Closes http://dev.plone.org/plone/ticket/9828
  [esteele, erikrose]

- User-add dialog will no longer hide errors (e.g., inability to mail).
  fixes http://dev.plone.org/plone/ticket/9964
  [smcmahon]

- Changed noform action for user add ajax overlay form to "reload" to
  fix http://dev.plone.org/plone/ticket/9957
  [smcmahon]

- Changed login form overlay handling to deal with the need for a redirect
  if logging in from pwreset_finish.
  Closes http://dev.plone.org/plone/ticket/5548
  [smcmahon]

- Changed the ``Add Plone site`` link in the ZMI to use the basic form. Too
  many regular users are still using the ZMI.
  [hannosch]

- Fix template errors in author_feedback_template.pt which prevented author
  feedback from being sent.
  Closes http://dev.plone.org/plone/ticket/9730
  [esteele]

- Update prefs_user_details.cpt and prefs_user_memberships.cpt templates to
  fit the current styling of other configuration screens.
  Closes http://dev.plone.org/plone/ticket/9660
  [esteele]

- Avoid leading spaces in the class attribute of the body element.
  Refs http://dev.plone.org/plone/ticket/9489.
  [dukebody]

- Removed explicit macros calls for related items from templates.
  Closes http://dev.plone.org/plone/ticket/9985
  [spliter]

- Deprecated document_relateditems.pt template - we are using viewlet instead.
  Refs http://dev.plone.org/plone/ticket/9985
  [spliter]

- Introduced order of viewlets for plone.belowcontentbody viewlet manager.
  Refs http://dev.plone.org/plone/ticket/9985
  [spliter]

- No longer show the ``Send this`` action by default. This refs
  http://dev.plone.org/plone/ticket/8800.
  [hannosch]

- Adjust login overlay position and width. Closes
  http://dev.plone.org/plone/ticket/9869.
  [dukebody]

- Adjust wording for user group membership removal. This fixes
  http://dev.plone.org/plone/ticket/9961.
  [dukebody]

- Make the ISiteRoot a INavigationRoot by default. This simplifies registering
  many views aimed at the nav root.
  [mj]

4.0a3 - 2009-12-21
------------------

- Updated statusmessages code to more modern API.
  [hannosch]

- Updated add-on configuration section. Clarified terminology to refer to
  de/activation and interpret product readme files as restructered text.
  [hannosch]

- Adjusted control panel and upgrade screens to show software instead of
  profile version and removed dependency on the persistent product registry.
  [hannosch]

- Changed the default profile metadata version to 4003, to follow our own best
  practices of distinguishing between profile and software versions.
  [hannosch]

- Added ``Plone site`` back to the all_meta_types list and revert change that
  made the site object not copyable. These prevented Plone sites from being
  imported from zexp files.
  [hannosch]

- Do not display the author contact form when the author has no email
  (for example for openid users).  Refs #8707.
  [maurits]

- Only specify icon_expr in factory type info; not also content_icon which
  has been deprecated in CMF 2.2.
  [davisagli]

- Optimize RSS template and make it work for items without a getText method.
  This closes http://dev.plone.org/plone/ticket/9696.
  [hannosch]

- Define encoding for RSS feeds. This closes
  http://dev.plone.org/plone/ticket/3506.
  [hannosch]

- On author.cpt, only display the "log in to add comments" button if mailhost
  is defined. Only show the mailhost warning if user is authenticated.
  [esteele]

- Adjusted rss_template to work for content items without an effective date
  and include issued and modified tags. Thanks for the patch anthonygerrard.
  This closes http://dev.plone.org/plone/ticket/7952.
  [hannosch]

4.0a2 - 2009-12-03
------------------

- Restore the ability to add Plone sites within ZODB mountpoints (and other
  OFS folders).
  [davisagli]

- Move prefs_navigation_form to plone.app.controlpanel as
  @@navigation-controlpanel. The form and its cpy script have been deprecated.
  [esteele]

- Use the @@plone-upgrade view as the default management screen for the
  migration tool.
  [davisagli]

- Respect multibyte language delimiter in search field. This closes
  http://dev.plone.org/plone/ticket/9422.
  [hannosch]

- RegistrationTool's registeredNotify now sends mail immediately instead of
  waiting until the end of the transaction. This puts the function back in
  line with the way the method worked in previous versions of Plone.
  http://dev.plone.org/plone/ticket/9871
  [esteele]

- Create normal folders instead of Large Folders (which are deprecated)
  for the initial example content.  All folders are now BTree-based.
  [davisagli]

- fixed validation of prefs_main_template for plonetheme.classic
  [spliter]

- re-applied fix for plone.css by aaronv. Fixes #9366 and #9761
  [spliter]

- moved plone.css.py to CMFPlone in order to share it among all themes
  http://dev.plone.org/plone/ticket/9366
  [spliter]

- moved "Manage portlets" fallback link out of main_template to
  plone.manage_portlets_fallback viewlet
  http://dev.plone.org/plone/ticket/9808
  [spliter]

- Point the "Join" action the newly-renamed @@register view.
  [esteele]

- Remove ``calendarpopup.js`` from jsregistry.xml. It no longer exists.
  [hannosch]

- Depend on ``plone.app.upgrade`` so it gets installed by default. Keeping
  the upgrade package separate only made sense when it had massively more
  dependencies than Plone itself. That cleanup isn't part of Plone 4.0.
  [hannosch]

- Added back an ``utranslate`` function to the i18nl10n module that retains the
  old call signature.
  [hannosch]

4.0a1 - 2009-11-19
------------------

- Moved ``Image Handling`` control panel into the main Plone category. It's not
  an add-on anymore.
  [hannosch]

- Clarified the default labels shown on the site setup overview page.
  [hannosch]

- Adjust tests to new Archetypes behavior, which respects the default language
  of the portal_languages tool.
  [hannosch]

- Adjust the _createObjectByType functions in utils and FactoryTool to use the
  _constructInstance method of the FTI instead of duplicating pieces of its
  logic.
  [davisagli]

- By default hide the "Subfolders" tab on collections. They don't behave in a
  way understandable to users. Existing sites aren't changed.
  [hannosch]

- Converted ``plone_javascript_variables.js`` to a browser page. Dynamically
  generating JS using a page template was too cumbersome. This also avoids the
  special ``escape_for_js`` handling of the translate script.
  [hannosch]

- "Relevance" was not internationalized in search_form.pt. This closes
  http://dev.plone.org/plone/ticket/9747
  [vincentfretin]

- "Your Plone site is up to date" was not internationalized in plone-upgrade.pt.
  This closes http://dev.plone.org/plone/ticket/9746
  [vincentfretin]

- "Preferences" link should go directly to the personal prefs, the memberprefs
  panel is an unnecessary abstraction here. Add-on products can easily add new
  links to the personal menu now, so that's the pattern we want to encourage.

- Removed the login portlet from the default setup now that the login link opens
  an inline window.
  [limi]

- Fixed a DYNAMIC_CONTENT in site_feedback_template.pt
  [vincentfretin]

- Make sure the 'Portlets: View dashboard' permission is set for Members.
  [davisagli]

- Make sure the mock MailHost used in tests is registered as a local utility
  so that it can be found via getToolByName.
  [davisagli]

- Moved all CSS styles to plonetheme.classic package. plonetheme.sunburst is
  now default theme, both are installed by default, classic theme may be
  uninstalled, sunburst theme can't be uninstalled.
  [limi, naro]

- Added site_encoding and bodyClass methods to the @@plone view. These should
  simplify main template a bit.
  [naro]

- Avoid AttributeError while getting the CMF version for the
  plone_control_panel when enable-product-installation is off in
  zope.conf.
  [maurits]

- Fixed bad internationalized messages in logged_out.pt
  [vincentfretin]

- Changed default message for label_show_all msgid from "Show all..." to
  "Show all items" in livesearch_reply.py to be the same as in folder_contents
  view which use the same msgid.
  [vincentfretin]

- Use the new ``pas_member`` view in the overview templates. This avoids
  getting the member info for each item in the listing from the PAS internals.
  [hannosch]

- registerNotify and mailPassword now send properly encoded emails.
  Fixes http://dev.plone.org/old/plone/ticket/9659
  [alecm]

- Deprecated register.py and join_form.cpt. This functionality has been moved
  to plone.app.users.
  [esteele]

- Changed ``listActions`` on the workflow tool to no longer call the
  ``listGlobalActions`` method on every installed workflow. This method would
  internally call and calculate the worklist (reviewer_queue) for every
  workflow. The listActions method is called by the workflow menu to show the
  state drop down menu on almost all pages.
  [hannosch]

- Deprecated the ``selectedTabs`` script in favor of a method on the
  GlobalSectionsViewlet.
  [hannosch]

- Micro-optimize the CatalogNavigationTabs view.
  [hannosch]

- Added a more prominent upgrade warning to the top of the ZMI screen, instead
  of the old tiny note on the portal migration tool.
  [hannosch]

- Added a new ``@@plone-upgrade`` view, which replaces the old migration tool
  DTML ZMI screens.
  [hannosch]

- Added a simple ``advanced`` mode to the add site form. If advanced is passed
  as a query argument to the ``@@plone-addsite`` more options are available.
  The button in the ZMI uses the advanced mode by default. Currently the choice
  of omitting the default content and deselecting any of the default extension
  profiles are limited to the advanced mode.
  [hannosch]

- Expose the site language in the add site form and refactor the language
  guessing based on the browser language into that view. The addPloneSite
  function takes an explicit argument for the language now.
  [hannosch]

- Hardcode utf-8 for UnicodeSplitter, since Hanno says that's all we
  can accept and there's no way to use getSiteEncoding from the splitter.
  [alecm]

- Added option to skip the creation of the default example content in the new
  add site form. Grouped the add-ons selection via a fieldset.
  [hannosch]

- Refactored the old factory dispatcher / addPloneSiteForm to use a modern
  browser page instead.
  [hannosch]

- Removed the special default page and translation handling. LinguaPlone uses
  a content language negotiator per default instead.
  [hannosch]

- Replaced highlightsearchterms.js with the Plone trunk
  jquery.highlightsearchterms.js plugin. This removes the need to add
  searchterm= query parameters to search.pt results.
  Refs. http://dev.plone.org/plone/ticket/8770
  [mj]

- Add a link to log out from the logged_out template if logged in as a Zope
  user via basic HTTP Authentication and the standard logout failed.
  [davisagli]

- Removed the cut/copy/paste icons from the action menu in new sites, as they
  just add noise + more HTTP requests.
  [limi]

- Moved happytalk in site_feedback_template.pt and author_feedback_template.pt
  to bottom of emails, per http://dev.plone.org/plone/ticket/7001
  [jonstahl]

- Added precedence: bulk header to several PasswordReset's
  mail_password_template, per http://dev.plone.org/plone/ticket/7000 - still
  haven't added this header to CMFPlone templates.
  [jonstahl]

- Added the upgrade warning to the main control panel screen. This is the same
  as found on the new overview page.
  [hannosch]

- Changed the new default overview page to be a normal browser page and made
  it aware of multiple Plone sites in the root or in ZODB mountpoints.
  [hannosch, davisagli]

- Overwrote the Zope quick start page, with a more helpful Plone specific
  version as already found in the unified installer.
  [hannosch]

- Turned the new add Plone site button in the ZMI into a link. This allows us
  to get out of the frameset to the top.
  [hannosch]

- Add jQueryTools integration, using plone.app.jquerytools.
  [smcmahon]

- Updated our add site ZMI screen.
  [hannosch]

- Changed search.pt (plone_forms) and rss_template.pt (plone_templates) so they
  display fullname instead of creator.
  [ralphjacobs]

- Cleaned up old an unused scripts to edit the plone site object itself. This
  is done via the site control panel now.
  [hannosch]

- Hide the TinyMCE profiles hidden from the Plone site add form.
  [robgietema]

- Added 'Use site default' to the wysiwyg_editor field in the Personal
  Preferences view.
  [robgietema]

- Set default value of wysiwyg_editor to blank (use site default).
  [robgietema]

- Added default editor property to the site properties.
  [robgietema]

- Added TinyMCE and set TinyMCE as default visual editor.
  [robgietema]

- Removed getProductInfo method from the migration tool. It wasn't used
  anymore and depended on the persistent product registry.
  [hannosch]

- Inlined the enableSyndication function into importFinalSteps in
  setuphandlers. Avoid an unneeded catalog search.
  [hannosch]

- Simplified portal creation code and got rid of the PloneGenerator class in
  setuphandlers. It was a useless closure for independent functions.
  [hannosch]

- Removed the `plone-site` import step and stop overriding the
  `componentregistry` step. The portal object directly implements the
  IObjectManagerSite interface, so we don't need to activate it as a site
  manager in an extra step anymore.
  [hannosch]

- Updated and added various ZMI-visible tool titles.
  [hannosch]

- Removed the `plone-archetypes` import step. This is handled via a normal
  GenericSetup dependency in metadata.xml.
  [hannosch]

- Merged the `plone_various` import step into the `plone-final` step and
  install more packages directly by their profiles.
  [hannosch]

- Removed the zserverPatch. There's not many people running ZServer as the
  front-end web server anymore, so this isn't particular useful.
  [hannosch]

- Fixed the default portlet blacklisting for the `Members` folder.
  [hannosch]

- Replaced Products.ATReferenceBrowserWidget with
  archetypes.referencebrowserwidget. This is PLIP 9258
  http://dev.plone.org/plone/ticket/9258
  [tom_gross]

- Clarified help text for extension profiles on the add site form.
  [davisagli]

- Added a mechanism for specifying profiles that are selected by default on
  the add site form. This should be kept in sync with PloneTestCase's list
  of default extension profiles.
  [davisagli]

- Hide the plonetheme.sunburst uninstall profile from the add site form.
  [davisagli]

- Default to plonetheme.sunburst for new sites.
  [esteele, davisagli]

- Allow email addresses as login name, with a switch on the security
  panel. This is plip 9214: Refs http://dev.plone.org/plone/ticket/9214.
  [maurits]

- Extend the language specific default configuration to set a reasonable first
  day of week on the calendar tool.
  [hannosch]

- Stop pretending to use GenericSetup's content import. As a last item we now
  create the translated front-page purely in imperative code. As a bonus we
  moved the body text of the front-page to a page template, so i18ndude can
  automatically extract it.
  [hannosch]

- Create and configure `Members` folder purely in setupPortalContent.
  [hannosch]

- Converted import and export steps XML files to use ZCML registrations.
  [hannosch]

- Made sure to have a complete list of non-installable profiles. No longer
  apply the filter to base profiles and ignore our default profile. This works
  in combination with the corresponding changes in quick installer to reduce
  portal creation time.
  [hannosch]

- Make use of the new `authenticated` flag for ResourceRegistries entries
  instead of specifying verbose condition expressions.
  [hannosch]

- "Categories" are now "Tags", in line with common usage and terminology.
  [limi]

- Changed workflow actor variable from user/getUserName to user/getId.
  http://dev.plone.org/plone/ticket/7398.
  [hannosch]

- Removed the AT graphviz references action from all content types.
  [davisagli]

- Finished switching tool and action icons to use PNG format.
  [davisagli]

- Exclude some of the CMFDefault functionality, that isn't used or usable
  inside Plone sites. The CMFDefault types are no longer supported.
  [hannosch]

- Move prefs_users_overview and prefs_groups_overview pages to
  plone.app.controlpanel (@@usergroup-userprefs and @@usergroup-groupprefs
  respectively).
  [esteele]

- Adjust to CMF's splitting of CMFCatalogAware into separate CatalogAware,
  WorkflowAware, and OpaqueItemManager mixins.
  [davisagli]

- Added zope.app.locales dependency, some strings are in zope domain such as
  'Invalid value' and '(no value)' found in portlet EditForm.
  [vincentfretin]

- Moved membershipRolemapping.dtml and portrait_fix.dtml to PlonePAS.
  [davisagli]

- Added icon_expr property to the Plone control panel tool actions, and
  switched to registering configlet icons here instead of in the action
  icons tool.
  [davisagli]

- Moved the diff tool registration to this package, so it can still be a tool
  for Plone 4.
  [davisagli]

- Use the new zope.ramcache in favor of zope.app.cache.
  [hannosch]

- Removed GroupUserFolder skin layers.
  [davisagli]

- Silenced the deprecation warning about old-style actions from CMFCore's
  ActionProviderBase when listing configlets with the control panel tool.
  [davisagli]

- Added the _IMREALLYPLONE4 hint to factory.py for PloneTestCase to use.
  [hannosch]

- Removed the calendar and review portlets from the standard global
  assignments. The review list is better put onto a personal dashboard and the
  calendar is exceptionally slow and rather user unfriendly. The news and
  events portlets are a better fit to show-case the portlets system.
  [hannosch]

- Include the `overrides.zcml` from `Products.PlacelessTranslationService` to
  actually make PTS' language negotiator available to the zope.i18n machinery.
  [hannosch]

- Got rid of the ToolNames indirection and declared the meta_types directly
  in the relevant tool class themselves.
  [hannosch]

- Moved ATCT specific exportimport code into the ATCT package itself.
  [hannosch]

- Made sure the plone.indexer registration works by introducing a more
  specific IPloneCatalogTool marker interface and registering the indexable
  object wrapper for this.
  [optilude]

- Added a restricted version of the opaqueItems method for CMFCatalogAware.
  This takes the idea of experimental.opaquespeedup one step further.
  [hannosch]

- Actually made the types tool action lookup optimization effective. Slightly
  optimized the add items drop-down menu.
  [hannosch]

- Removed the `ResourceRegistries` skin layer. It only contained test code.
  [hannosch]

- Make use of the new IContainer API of object managers and replace objectIds
  and objectValues calls.
  [hannosch]

- Finally removed the interfacePatch for the IContainer interface of
  OFS.ObjectManager after it has been merged upstream.
  [hannosch]

- Removed CMFTopic from our dependency list, it turns out that we aren't
  actually using any of it.
  [hannosch]

- Added proper deprecation warnings for the IBrowserDefault,
  IDynamicViewTypeInformation and ISelectableBrowserDefault interfaces, who
  has always come from Products.CMFDynamicViewFTI.
  [hannosch]

- Use the `replace_local_role_manager` method from borg.localrole.
  [hannosch]

- Deprecate our own IOrderedContainer interface in favor of the original one
  from OFS.
  [hannosch]

- Avoid dependency on the zope.app.zapi package.
  [hannosch]

- Declare package dependencies and fixed deprecation warnings for use
  of Globals.
  [hannosch]

- No longer depend on the PageTemplates.GlobalTranslationService but use
  zope.i18n directly.
  [hannosch]

- Merged in more performance optimizations from experimental.contentcreation.
  We don't restrict the permissions for the temporary folder anymore, but
  only care about the permissions of the actual target folder.
  [hannosch]

- Use the new `icon_expr` for specifying icons for content types instead.
  [hannosch]

- Prefer path expressions over Python expressions for persistent expressions.
  [hannosch]

- Fixed the content_status_history form to include the required content table.
  The old_folder_contents template is gone.
  [hannosch]

- Fixed the browserDefault tests to use actual traversal to look up views
  for content items instead of relying on Acquisition.
  [hannosch]

- Moved the `scale_image` function from utils into the PlonePAS.utils
  module, as PlonePAS is the only user of it.
  [hannosch]

- The remaining functionality from GroupUserFolder has been merged into
  the PlonePAS package. GroupUserFolder is no longer required.
  [hannosch]

- Removed the groups, groupdata, membership and memberdata tools from this
  package. All code is now in a central place inside PlonePAS. The persistent
  tools have been from the PlonePAS package since Plone 2.5.
  [hannosch]

- Replaced has_key method calls with containment checks via `in`.
  [hannosch]

- Replaced a direct interface invocation with a queryAdapter call, to avoid
  an internal getattr call and make the pattern clearer.
  [hannosch]

- Replaced here with context in all templates and scripts. The old spelling is
  still supported, but we need to settle on one to avoid confusion.
  [hannosch]

- Optimized the types tool action lookup further to avoid Acquisition lookups.
  [hannosch]

- Simplified the normalizeString method.
  [hannosch]

- Optimized the action lookup code and implemented category restriction for
  the types tool in the same way it was available for the actions tool.
  [hannosch]

- Removed remaining sys.modules hacks to provide the browser.ploneview as
  browser.plone.
  [hannosch]

- Removed last unused external methods and PloneInitialize code. To my
  knowledge the Windows installer doesn't use this code anymore.
  [hannosch]

- Write the doctype definition in the main_template in a way that does not
  claim to be valid XML, as the main_template really isn't.
  [hannosch]

- Worked around `sys._getframe` call in mark_view.
  [malthe, hannosch]

- Removed macro slot for changing the document type; this was not
  correct XML and should this flexibility be required, it's
  recommended to customize `main_template.pt`.
  [malthe]

- Turned deprecated string 'Unauthorized' exceptions into real exceptions.
  [davisagli]

- Removed module alias for the ploneview formerly named plone.
  [hannosch]

- Clarified content language versus response language handling.
  [hannosch]

- Removed unmaintained and unused Favorite content type.
  [hannosch]

- Removed our own home-grown dependency checking code.
  [hannosch]

- Exposed option to honour exclude from navigation even in subfolders from
  navtree_preferences.  Request from theming sprinter at ploneconf2008.
  [MatthewWilkes]

- Made the fieldset tabbing code faster on startup (especially for IE) by
  constructing a big string and creating the HTML elements in one bunch
  instead of using DOM functions to add them step by step.
  [fschulze]

- Added uniqueItemIndex as a method to the plone view.
  [hannosch]

- Added back ``global_defines.pt`` as a template including the (empty)
  macro definition. This allows main templates to be compatible with both
  Plone 3.x and 4.0 at the same time.
  [hannosch]

- Removed ``global_defines.pt`` and the globalize-hack. Templates
  now bring in their tool and function dependency using the
  standard utility views or via normal Acquisition of tools.
  [malthe, hannosch]

- Fixed test for editing language fields. This refs
  http://dev.plone.org/plone/ticket/8342.
  [hannosch]

- Removed deprecated context parameter in getDefaultPage and
  isDefaultPage in utils.py.
  [maurits]

- Made sure the export order of the factory tool GS step is consistent.
  This closes http://dev.plone.org/plone/ticket/7892.
  [hannosch]

- Replaced lock_icon with smaller version with one third of the size.
  [hannosch]

- Removed backwards-compatibility code in calendar_formfields.js introduced
  in Plone 3.1.4. Any date-time picker not based on calendar_macros.pt
  using the old-style (no plone.jscalendar namespace) methods will no
  longer work until adjusted.
  [mj]

- Don't show relevance information of one percent in the search form,
  since sort_on searches will always show this for all entries
  This closes http://dev.plone.org/plone/ticket/4325
  [hannosch]

- Removed duplicated isMemberIdAllowed method from registration tool.
  [hannosch]

- Fixed mailto link in event view and enhanced the spam protect script to
  allow setting css ids on the generated anchor tag. This closes
  http://dev.plone.org/plone/ticket/8219
  [hannosch]

- Fixed contact form to be usable for authenticated users which have no
  email address stored in their member data. This closes
  http://dev.plone.org/plone/ticket/5766
  [hannosch]

- Avoid empty tags in the contact form. This closes
  http://dev.plone.org/plone/ticket/8182
  [hannosch]

- Avoid an empty div in login_form. This closes
  http://dev.plone.org/plone/ticket/8192
  [hannosch]

- Avoid an empty dd in recently modified.pt. This closes
  http://dev.plone.org/plone/ticket/8186
  [hannosch]

- Avoid an empty span in folder_summary_view. This closes
  http://dev.plone.org/plone/ticket/8181
  [hannosch]

- Changed wording in personalize form to remove reference to external
  editor icon and add a note about ZopeEditManager. This closes
  http://dev.plone.org/plone/ticket/7390
  [hannosch]

- Changed webstats_js in portal properties to a text field.
  This refs http://dev.plone.org/plone/ticket/7781
  [hannosch]

- Added option to the error log control panel to search for an error log
  entry by number, since the number is the only thing that is exposed to
  normal users. This closes http://dev.plone.org/plone/ticket/7234
  [hannosch]

- Changed title of collections control panel to plural form. This
  closes http://dev.plone.org/plone/ticket/8096
  [hannosch]

- Include link to the plone.org upgrade manual from the migration tool
  inside the ZMI. This closes http://dev.plone.org/plone/ticket/8075
  [hannosch]

- Clarify help text in content_status_history. This closes
  http://dev.plone.org/plone/ticket/8218
  [hannosch]

- Let default RSS list publication date, not modified date and include
  the body text. This closes http://dev.plone.org/plone/ticket/7952
  [hannosch]

- Updated the check_id script to disallowed content by the name of
  properties. This closes http://dev.plone.org/plone/ticket/6005
  [hannosch]

- Fixed invalid markup in membershipRolemapping.dtml. This closes
  http://dev.plone.org/plone/ticket/6222
  [hannosch]

- Removed long unused getObjPositionInParent.py script which wasn't
  functional at all anymore, since it used Zope 2 interfaces. Also
  simplified the getObjPositionInParent function in the CatalogTool.
  This closes http://dev.plone.org/plone/ticket/6081
  [hannosch]

- Removed getActionObject call from createObject script. It was a private
  method and would always fail. This closes
  http://dev.plone.org/plone/ticket/7172
  [hannosch]

- Removed testing of sendto action visibility from sendto.cpy. There's a
  permission to use to restrict sending mail. This closes
  http://dev.plone.org/plone/ticket/5377
  [hannosch]

- Disable external editor icon for structural folders. This closes
  http://dev.plone.org/plone/ticket/6871
  [hannosch]

- Updated the check_id script to disallowed content by the name of zip or
  plone since this shadows the views by those names. This closes
  http://dev.plone.org/plone/ticket/6105
  [hannosch]

- Purged old Zope 2 Interface interfaces for Zope 2.12 compatibility.
  [elro]

- Make use of upgrade steps with a source '*' version and an explicit
  destination, to register the 'enable site' and 'register tools as
  utilities' only once.
  [hannosch]

- Added support for upgrade step groups to the migration tool and started
  exposing the individual upgrade methods as steps.
  [hannosch]

- Changed the way messages are handled during migration. We don't pass an
  `out` list around anymore, but use the logging framework.
  [hannosch]

- Replaced our own migration step registration by using GenericSetup steps
  directly. Changed the migration tool to integrate with GS instead.
  Added BBB code to read the instance version from the migration tool if
  the last profile version isn't set yet inside the GS tool.
  [hannosch]

- Exposed all our migration steps as GenericSetup upgrade steps.
  [hannosch]

- Hide the deprecation warning about the moved ITranslatable interface
  for our own code.
  [hannosch]

- Use png icons instead of gif icons since they are much more flexible
  for styling.
  [dannyb, wichert]

- Fixed the coreVersions method in MigrationTool to return strings and not
  bound methods for the Zope and Python version.
  [hannosch]

- Fixed off-by-two error in transaction_note. This closes
  http://dev.plone.org/plone/ticket/7610
  [hannosch]

- Moved all icons for real actions from the action icons tool to the
  actions themselves.
  [hannosch]

- Changed PloneTool's getIconFor method to prefer the icon expression set
  on the action itself instead of looking it up in the action icons tool.
  This finally makes use of the new icon expression on actions introduced
  in CMF 2.1.
  [hannosch]

- Avoid unneeded line breaks in TAL output, by effectively disabling the
  internal beautified wrapping inside tags. This reduces the HTML output
  by 5% - 10% for normal Plone pages.
  [hannosch]

- Memoize the installed products and packages in App.FactoryDispatcher
  for the duration of the process runtime.
  [hannosch]

- Hiding page history, page navigation, and busy icon (spinner) in print.css
  Related to http://dev.plone.org/plone/ticket/7433
  http://dev.plone.org/plone/ticket/7402
  [siebo]

- Updated webdav_enabled method in utils.py to check for
  webdav.interfaces.IWriteLock interface in addition to the old Zope2
  interface.
  [hannosch]

- Use a FauxArchetypeTool which returns no catalogs for CatalogMultiplex
  aware objects in portal factory. This prevents most temporary objects
  from being indexed in the first place.
  [tesdal, hannosch]

- Move our GenericSetup import step registrations to zcml.
  [wichert]

- Added a 'do-not-use' warning to the ZMI security screen for Plone content
  objects. Sharing tab or workflows are what you are looking for.
  [hannosch]

- Moved interface declarations for factorytool from ZCML to the class.
  [hannosch]

- Added BBB code for ITranslatable, which is now part of LinguaPlone.
  [hannosch]

- Added an explicit button to add a new Plone site to the ZMI for faster
  access. If you have installed Plone this is probably what you want to
  add most of the time. The button only shows up in the root folder.
  [hannosch]

- Deprecate the ITranslatable interface. This interface is LinguaPlone-
  specific and has thus been moved to LinguaPlone.
  [wichert]

- Removed tests for isRTL method of PTS. The method was deprecated in the
  last release and is gone now.
  [hannosch]

- Removed PTSTranslationDomain utilities. PTS exposes all translation files
  as pure Zope3 translation utilities now, so these aren't needed anymore.
  [hannosch]

- Replaced our FasterStringIO implementation by one based on
  collections.deque, which is a faster than StringIO.
  [hannosch]

- Removed more deprecated code, adjusted some comments.
  [hannosch]

- Tweaked sortable_title method to give reasonable results for titles with
  many numbers in them, like '1.2.3 document'.
  [hannosch]

- Moved CMF skins registration into configure.zcml, removed security
  declaration for no-longer extant listPolicies of the portal.
  [hannosch]

- Refactored initial content creation into a separate extension profile,
  thus making it possible to skip it. This refs
  http://dev.plone.org/plone/ticket/6948
  [hannosch]

- Removed some outdated Extension scripts.
  [hannosch]

- Removed deprecated tool related Zope2 interfaces. Extended the
  deprecation period for ConstrainTypes and NonStructuralFolder as these
  are still used in Plone Core.
  [hannosch]

- Removed work-around code for insertion of non-unicode non-ascii non-utf8
  encoded text in TAL. This will produce an error now. Always use Unicode
  when using data in page templates and TAL.
  [hannosch]

- Removed lots of deprecated code and zcml registrations.
  [hannosch]

- Fixed ticket #9420 DC.date.valid_range not emitted if only Publishing Date is set.
  [jaroel]


3.3.6 - Unreleased
------------------

- Fixed http://dev.plone.org/plone/ticket/10510.
  [gborelli, simahawk, sauzher]

- Added doctests to members search.
  [gborelli, simahawk, sauzher]

- Fixed not translatable messages in advanced form: "Hide the search form" and
  "Edit your search options".
  [gborelli, simahawk]

- Fixed http://dev.plone.org/plone/ticket/10486.
  [gborelli, simahawk]


3.3.5 - March 3rd, 2010
-----------------------

- Check for existence of a hash in the location before attempting to scroll to
  that location in toc.js. Fixes bug introduced in r32066, and refs
  http://dev.plone.org/plone/ticket/9364
  [dunlapm]


3.3.4 - January 14th, 2010
--------------------------

- member_search_results display login names only if the user
  has "List portal members" permission.
  Return "not allowed" message and empty search results if not.
  This fixes http://dev.plone.org/plone/ticket/9923
  [khink]

- In the MockMailHostTestCase register and unregister the mock mail
  host as an IMailHost.  Fixes a test failure in PasswordResetTool
  (once I let that use this test case).  Change taken over from Plone
  trunk.
  [maurits]

- Do not display the author contact form when the author has no email
  (for example for openid users).
  Refs http://dev.plone.org/plone/ticket/8707
  [maurits]


3.3.3 - December 8, 2009
------------------------

- Don't add a .zem extension for the external editor except on OS X. This
  closes http://dev.plone.org/plone/ticket/9888
  [tbenita, davisagli]

- Added tal condition to check if the user object is None when rendering
  pref_group_members.cpt since group assignments are not deleted when
  a user is deleted.
  This addresses http://dev.plone.org/plone/ticket/9885
  [vangheem]

- Increased maximum length of the sortable_title index from 30 to 40 characters
  to ensure titles containing an ISO date can be sorted.
  [hannosch]

- Added scroll to anchor tag in toc.js because Firefox was not bringing a user
  to any anchor tags when a link was directly given to one.
  This closes http://dev.plone.org/plone/ticket/9364
  [vangheem]

- Fixed untranslatable info message "The username you entered could not be
  found" and other messages in RegistrationTool.py.
  This closes http://dev.plone.org/plone/ticket/9744
  [vincentfretin]

- Configlets title can now use a different domain than plone.
  This closes http://dev.plone.org/plone/ticket/9738
  [vincentfretin]

- Fixed "Manage portlets" not translated when there is no portlet visible.
  This closes http://dev.plone.org/plone/ticket/8454
  [vincentfretin]

- Better validation and error messages for group create/edit form.
  Fixes http://dev.plone.org/plone/ticket/9667
  [lzdych]

- plone.css will now output stylesheets with link rendering
  Fixes http://dev.plone.org/plone/ticket/9366

  sitemap template now displays objects without a value for Title
  applied patch from crchemist
  Fixes http://dev.plone.org/plone/ticket/9775
  [aaronv]

- Removed option "Send a mail with the password" from the join form,
  as we never send an email with the password.
  Refs http://dev.plone.org/plone/ticket/9670
  [maurits,vincentpretre,jladage]

- Buttons on discussion form are now hidden from print view.
  Fixes http://dev.plone.org/plone/ticket/8460
  [lzdych]

- Added missing migration step to update permissions on "legacy"
  workflows for new roles. Thanks to Vitaliy Podoba for the patch.
  This fixes http://dev.plone.org/plone/ticket/8905
  [amleczko]


3.3.2 - November 3, 2009
------------------------

- Shift "Item type" options under the advanced search page to the right
  when viewed for RTL scripts. This fixes
  http://dev.plone.org/plone/ticket/9666
  [emanlove]

- Make sure the folder_listing, folder_summary_view, and folder_tabular_view
  call getText with a full acquisition chain (but make the conditional for
  whether to display text test for the existence of getText on the aq_base'd
  context to avoid accidental acquisition).  This fixes
  http://dev.plone.org/plone/ticket/8463
  [davisagli]

- Use PlonePAS methods for adding and removing members from groups, as well
  as for listing group membership. These methods are PAS aware and thus work
  correctly with PAS plugins other than the GroupUserFolder. Thanks to
  Giovanni Toffoli for the initial patch.
  Fixes http://dev.plone.org/plone/ticket/9163
  [mj]

- Fix linkintegrity-related issue regarding missing undo log entries after
  removing content via the "delete" action.
  This fixes http://dev.plone.org/plone/ticket/7784
  [witsch]

- Show template id or view name in <body class="template-..">. There was
  template id only before.
  http://dev.plone.org/plone/ticket/9111
  [naro]

- Check AddPortalContent permission before calling invokeFactory from
  FactoryTool.
  http://dev.plone.org/plone/ticket/8748
  [naro]

- Added helper methods to the i18nl10n method, to change the default date and
  time formats used by zope.i18n.locales. This makes it easier to use a 24
  hour clock in the date/time widgets for English speakers.
  [hannosch]

- Removed msgids in portlets.xml. There is no support for
  msgids in the import of portlets.xml implementation.
  This allow to extract translatable strings with i18ndude.
  This closes http://dev.plone.org/plone/ticket/9631
  [vincentfretin]

- Fixed some duplicated msgids with different defaults.
  There is no new strings to translate.
  See http://dev.plone.org/plone/ticket/9633
  [vincentfretin]

- Make the external_editor link on OS X use the .zem extension.
  Fixes http://dev.plone.org/plone/ticket/7291
  [optilude]

- Minor or trivial changes and fixes to many templates for obtain
  code that is also XHTML Strict
  See http://dev.plone.org/plone/ticket/4379
  [keul]

- Fixed *folder_constraintypes_form.cpt* template; was XHTML invalid when
  showing portal type with whitespaces (like "News Item")
  [keul]

- Fixed handling of URL fragment identifiers in form-tabbing. This closes
  http://dev.plone.org/plone/ticket/9500
  [mj]


3.3.1 - September 9, 2009
-------------------------

- Defined the portal_url variable to
  context/@@plone_portal_state/navigation_root_url
  in author.cpt and personalize_form.cpt. Plone 4 and trunk are not impacted.
  This closes http://dev.plone.org/plone/ticket/9453
  [vincentfretin]

- Fix ITranslatable to use the canonical interface from LinguaPlone or fall
  back to a Zope3-style interface.
  [hannosch, witsch]

- Fixed a bug which deletes an object in the acquisition path instead of
  the original object in case of a catalog inconsistency. This closes #9046.
  [pilz]


3.3 - August 18, 2009
---------------------

- Fix broken IE6 CSS support.
  [spliter]


3.3rc5 - August 1, 2009
-----------------------

- Remove trailing space from
  history_compare_with_previous_inline.png.metadata filename.
  This fixes http://dev.plone.org/old/plone/ticket/9367
  [wichert].

- Modified the history viewlet style so actions are green without
  background and border. Messages are on a blue background.
  [vincentfretin]


3.3rc4 - July 7, 2009
---------------------

- Added migration step to fix missing cooked expressions in
  portal_css, which could mess up the site UI.  Fix by Tom Gross.
  Fixes http://dev.plone.org/plone/ticket/9141
  [maurits]

- Upgrade to jQuery 1.3.2. This fixes multiple bugs on various browsers,
  allows use of more jQuery plugins (particularly current versions of
  jQuery UI). The only BBB problem I am aware of is use of the @ in
  attribute selectors (as in a[@target=_blank]), which has been deprecated
  for a long time and is no longer supported in jQuery 1.3.
  [wichert]

- Make the BBB support for registerIndexableAttribute() more robust by only
  registering the indexer adapters when ZCML is loaded. This should fix
  issues with functional tests written for older versions of Plone.
  [optilude]

- Don't rely on a Zope 2 style interface in the getObjPositionInParent
  indexer - accept the proper Zope 3 interface for IOrderedContainer as well.
  [optilude]

- When viewing the prefs_install_products_form, do not do inline
  migration for profiles that were previously unknown as this may hide
  valid upgrade steps in some cases.
  [maurits]


3.3rc3 - May 22, 2009
---------------------

- Hide the NuPlone uninstall profile from the list of available extensions
  at Plone site creation.
  [wichert]

- mark_special_links.js: Fix jQuery syntax for element wrapping. This closes
  http://dev.plone.org/plone/ticket/8200
  [dunlapm]

- form_tabbing.js: Allow for selection of a fieldset tab other than the default
  if a url hash is in the form of #fieldset-[fieldsetname]. This allows for
  graceful fallback if JavaScript is disabled.
  [dunlapm]

- Show old and new profile versions for products with profile, this closes
  http://dev.plone.org/plone/ticket/9172
  [vincentfretin]

- Removed width from eventDetails CSS class, this closes
  http://dev.plone.org/plone/ticket/8933
  [vincentfretin]

- Split label_event_byline into two in folder_summary_view.pt like in
  folder_listing.pt fixed in Plone 3.3rc1, this closes
  http://dev.plone.org/plone/ticket/8358
  [vincentfretin]

- Removed spurious comma from unlockOnFormUnload.js which was causing
  Javascript errors in IE.  This closes http://dev.plone.org/plone/ticket/9157
  [davisagli]

- Split description_no_account msgid into two, heading_new_user msgid added.
  [vincentfretin]

- Added Internet Explorer 8 support. We only load the workaround CSS file for
  IE7 and earlier now, Internet Explorer 8 parses the
  '<meta name="IE" content="EmulateIE8" />' header that forces it into standards
  mode on both intranets and public internet sites.
  [limi]

- author.cpt should honour allowAnonymousViewAbout in the same way as
  document_byline, this closes http://dev.plone.org/old/plone/ticket/8560
  [elro]


3.3rc2 - April 5, 2009
----------------------

- Added an explicit return statement in the upgrade code for products without
  a GS profile. Thx to Vincent Fretin for the code review.
  [hannosch]

- Fixing permissions typo in object_rename button, this closes
  http://dev.plone.org/plone/ticket/9060
  [siebo]


3.3rc1 - March 30, 2009
-----------------------

- New favicon.ico that is in line with the new branding.
  [limi]

- author.pt: Fixed the #region-content mess, replaced modification date with
  created date (as that's what the table says it's listing), reduced to 5 items
  instead of 30 tables with 5 items each, made the table vertical.
  [limi]

- batch_macros.pt: Added "current" class to current item, removed the brackets,
  added ellipses. Moved comments to a tal section to stop them from showing up
  in the source.
  [limi]

- default_error_message.pt: Turned apostrophes into real apostrophes.
  [limi]

- join_form.pt: Removed unnecessary fieldset.
  [limi]

- logged_out.pt: Removed duplicate "new account" section (it's actually located
  in the login form).
  [limi]

- login_form.pt: Moved Forgot/New out of the fieldset, fixed wording + added
  headline.
  [limi]

- main_template.pt: Moved #content to main template instead of offloading its
  responsibility to the individual templates. This makes it easier to avoid
  duplication and make it possible to use it with Deliverance and similar
  theming approaches.
  [limi]

- personalize_form.pt: Cleaned up the #content mismatch. No more double tabs.
  [limi]

- search_form.pt: Removed unnecessary fieldset, inserted "searchform" id on
  form to not get it filled in as id="search" automatically.
  [limi]

- Updated the custom indexes in CatalogTool.py to no longer depend on the
  'portal' keyword or kwargs, both of which are gone from plone.indexer.
  This is done in an effort to be forward-compatible with CMF 2.2. See
  the plone.indexer README for more details.
  [optilude]

- Merged `safe-upgrade-button` branch. Instead of the removed `Reinstall`
  button in the `Add/Remove products` control panel, we now have an upgrade
  button for all products whose installation is driven by GenericSetup. This
  is based on GenericSetup upgrade steps.
  [hannosch]

- Fixed msgid label_event_byline default message which contained dynamic content.
  Created a label_event_byline_without_location used when you don't specify
  location in an Event.
  [vincentfretin]

- Updated the custom indexes in CatalogTool.py to no longer depend on the
  'portal' keyword or kwargs, both of which are gone from plone.indexer.
  This is done in an effort to be forward-compatible with CMF 2.2. See
  the plone.indexer README for more details.
  [optilude]

- Fixed the registerIndexableAttribute() backwards-compatibility shim to
  register named adapters.
  [optilude]

- Re-added the 'getRemoteUrl' and 'link_remote' attributes of the navtree
  decorator, which were lost during the implementation of PLIP 126.  Note
  that these attributes are deprecated and will not be available in Plone 4.
  Custom navigation templates using these attributes should simply link to
  the Link object, whose default view now takes care of redirecting based on
  the value of the global 'redirect_links' property.
  [davisagli]

- Make the Groups Overview search post back to the same page, since it displays a
  lot more useful information than the prefs_user_group_search, and fits more
  with the way the Users Overview works. Include a "Show all" button as well.
  [esteele]


3.3b1 - March 12, 2009
----------------------

- Replace the workflow history portlet with a content history portlet
  for newly created sites. This implements PLIP 243.
  [wichert]

- Changed most actions to now use the globals_view/navigationRootUrl. Updated
  the CMFCalendar tool override to allow the calendar portlet to allow passing
  in kwargs such as path.  Fixed skin templates and scripts to use the
  @@plone_portal_state/navigation_root_url instead of portal_url.
  This implements http://plone.org/products/plone/roadmap/234
  [calvinhp]

- Removed CatalogTool.ExtensibleIndexableObjectWrapper in favour of the
  wrapper in plone.indexer, and made registerIndexableAttribute() a deprecated
  facade for registering an IIndexer adapter. See plone.indexer for more
  information about the correct (and more robust) way to register custom
  indexers.
  [optilude]

- Removed the `Reinstall` button from the `Add/Remove products` control panel.
  Users would constantly mistake it as an upgrade mechanism, which Plone does
  not yet support in a structured way.
  [hannosch]

- Added an option in the Site Settings configlet to disable TTW locking
  entirely.  Also fixed a couple bugs with unlocking and made it so the
  lock gets refreshed as long as an editor is on the edit page.
  This implements http://plone.org/products/plone/roadmap/240

- Added a 'redirect_links' site property and corresponding 'Redirect
  immediately to link target' setting in the types configlet (for the Link type
  only).  The default view for the Link type has been changed to
  link_redirect_view.py from the plone_content skin layer, which redirects or
  falls back to the old link_view depending on the 'redirect_links' value.
  This implements http://plone.org/products/plone/roadmap/126
  [davisagli]

- "Mark external links" and "External links open in new window" were not working
  independently ('mark' had to be set for 'new window' to work) and marking could
  not be turned off at all (#7383). Fixed by having either one enable the js
  support and adding a new site property to control marking. Implemented so
  that new site property will be assumed false if missing and created on change
  if missing -- so no migration required. There is a matching change in
  plone.app.controlpanel.
  [smcmahon]

- PLIP 238: Disable inline editing for new Plone sites.
  [wichert]


3.2.2 - March 3, 2009
---------------------

- Register 3.2 -> 3.2.1 migration step with the migration machinery. This fixes
  problems due to a missing site  property for migrated sites.
  [matthewwilkes]

- Fix the internalization of folder_rename status message
  http://dev.plone.org/plone/ticket/8750
  [encolpe]


3.2.1 - February 4, 2009
------------------------

- Add dependency on Products.NuPlone to prevents sites who use NuPlone from
  breaking when upgrading from Plone 3.0.x or 3.1.x to 3.2 or later.
  [wichert]

- Fix contact_info.cpt so it bases the appearance of the fullname and email
  fields on whether they are set in the current member's profile, rather
  than on whether the current user is anonymous or not.  This closes
  http://dev.plone.org/plone/ticket/8526
  [davisagli]

- Update default frontpage to refer to Plone 3 instead of 3.0.
  [wichert]

- Added time_only for use with toLocalizedTime so that event_view now localizes
  the start/end times if the start/end dates are the same. Added migration for
  3.2 to 3.2.1 to add new property to the property tool. Closes
  http://dev.plone.org/plone/ticket/8607
  [jnelson, calvinhp]

- Fixed links-plain issue on the front-page. This closes
  http://dev.plone.org/plone/ticket/6479.
  [cwainwright, calvinhp]

- Put in workaround for IE6 background caching problem, closes
  http://dev.plone.org/plone/ticket/7445
  [cwainwright, calvinhp]

- Removed old background icon from personal bar for RTL scripts.
  Closes http://dev.plone.org/plone/ticket/4570
  [emanlove]

- Moved history icon off text and shifted history header
  to the right under RTL scripts. Closes
  http://dev.plone.org/plone/ticket/6368
  [emanlove]

- Cleaned up document actions for RTL scripts. Closes
  http://dev.plone.org/plone/ticket/8863
  [emanlove]


3.2 - December 31, 2008
-----------------------

- Merge the upgrade instructions from
  http://plone.org/documentation/manual/upgrade-guide/version/upgrading-from-3-x-to-3.2
  into the release notes.
  [wichert]


3.2rc1 - December 15, 2008
--------------------------

- Shifted profile and personal preferences to the left for RTL
  scripts. Closes
  http://dev.plone.org/plone/ticket/8169
  [emanlove]

- Load the `plone.app.locales` configure.zcml. This fixes
  http://dev.plone.org/plone/ticket/8788.
  [hannosch]

- Cleaned up Livesearch results for RTL Languages.
  Closes http://dev.plone.org/plone/ticket/4632
  [emanlove]

- For RTL languages adjusted document content padding so welcome
  text fits inside text area. Closes
  http://dev.plone.org/plone/ticket/6919
  [emanlove]

- For RTL languages shifted portrait photo to the left.
  Closes http://dev.plone.org/plone/ticket/6214
  [emanlove]

- Added 'context' as an alias for 'object' in action expressions.
  [davisagli]

- Include missing dependency on plone.app.locales.
  [hannosch]

- Moved plone specific diff tool configuration back to Plone default
  profile, since it's both plone specific and was never actually added
  to CMFDiffTool.
  Closes http://dev.plone.org/plone/ticket/8590
  [alecm]

- Fixed Forbidden error when attempting to login for the first time as a newly
  created user, if the must_change_password property has been added (as a
  Boolean) to the portal_memberdata tool and set to True.
  Closes http://dev.plone.org/plone/ticket/8425
  [hexsprite]

- Fixed the toc.js to not turn heading text containing an "@" into the link.
  Closes http://dev.plone.org/plone/ticket/7949
  [sbruno, calvinhp]

- Fixed the form_tabbing to use the correct buttons names. Closes
  http://dev.plone.org/plone/ticket/7559
  [lucie, calvinhp]

- Fixed the full_review_list select all link to only select the items shown
  and not all of the items at the portal root. This closes:
  http://dev.plone.org/plone/ticket/6991
  [garbas, calvinhp]

- Gave RTL.css higher priority within the stylesheet registry.
  loses http://dev.plone.org/plone/ticket/8505
  [emanlove]

- For RTL languages shifted Info Bar to the right.
  Closes http://dev.plone.org/plone/ticket/8140
  [emanlove]

- For RTL languages shifted comment icon to the right.
  Closes http://dev.plone.org/plone/ticket/6366
  [emanlove]


3.2a1 - October 11, 2008
------------------------

- Take getNotAddableTypes into account when determining if the editable
  border should be shown.
  [wichert]

- First fully eggified Plone release (ignoring the not yet eggified
  Zope2).
  [wichert]


3.1.7 - November 5, 2008
------------------------

- Updated the PloneTool normalization tests to match plone.i18n policies.
  [hannosch]


3.1.6 - October 7, 2008
-----------------------

- PloneTool.reindexOnReorder: Don't fail if the catalog contains stale
  entries.
  [stefan]

- Fixed the silent fail of the group membership from a user via the
  prefs_user_memberships form. This closes
  http://dev.plone.org/plone/ticket/8468
  [garbas, calvinhp]

- Fixed the migration from 3.0.1 to 3.0.2 to now put back the actionicons
  for the languages control panel.
  This closes http://dev.plone.org/plone/ticket/7901
  [KurtB, calvinhp]

- Changed isIDAutoGenerated to work with types that have .'s in them in the
  case that namespaces are included in the type's portal_type. For example:
  collective.types.ExternalSearch (to pick one from the collective). This
  closes http://dev.plone.org/plone/ticket/8480.
  [pbugni,dunlapm]

- Changed prefs_group_members.pt search table to behave coherently with
  prefs_users_overview.pt, including the results header only when
  there are results to show.
  [igbun]

- By default, keep the styling when managing portlets separate from the
  styling when viewing the portlets, to improve usability with custom
  themes.  This closes http://dev.plone.org/plone/ticket/8391
  [davisagli]

- Fixed syntax error in prefs_group_details.pt that prevented the saving
  of lines fields as well as an error that caused groups to sometimes display
  "()" as the contents of a previously undefined lines field. This closes
  http://dev.plone.org/plone/ticket/8427. Thanks to michaellaunay for the
  updated bugreport and included fix.
  [dunlapm]

- Fixed link to author.cpt from personalize_form so it works for
  users with URLs for a user id (e.g. OpenID users).  This closes
  http://dev.plone.org/plone/ticket/8040
  [davisagli]

- Fixed link to dashboard from personalize_form so it only shows
  if the user has permission to view the dashboard.
  [davisagli]

- Fixed font-size of the text in input text fields in IE.
  Closes http://dev.plone.org/plone/ticket/8412
  [spliter]

- Fixed the width for rediculously wide buttons in IE.
  Closes http://dev.plone.org/plone/ticket/8411
  [spliter]

- Fix non XML syntax compliant ids in contentmenus. This closes
  http://dev.plone.org/plone/ticket/8195
  [garbas,calvinhp]

- Avoid 'TypeError: getTypeInfo' on the default error page when
  the parent of the item that cannot be found is a resource
  directory.
  [maurits]


3.1.5 - August 19, 2008
-----------------------

- Made the have_portlets method from the plone view available to anonymous
  users as done on Plone trunk.
  [hannosch]

- Fixed incorrect translation handling of content created within
  PloneGenerator.setupPortalContent. Thanks to Erico Andrei for the
  hard work! This closes http://dev.plone.org/plone/ticket/8379.
  [deo]

- Removed duplicate settings in setuphandlers.py that are managed by GS
  profiles. This closes http://dev.plone.org/plone/ticket/8351 and
  http://dev.plone.org/plone/ticket/8352.
  [dunlapm]

- Avoid triggering a DeprecationWarning when passing a context
  parameter from our utils.py versions of getDefaultPage or
  isDefaultPage to their counterparts in plone.app.layout.
  Instead we show a warning ourselves when passed a context; the
  context is ignored.
  [maurits]

- Avoid acquiring getText from parent objects in all folder views. This
  closes http://dev.plone.org/plone/ticket/8190.
  [hannosch]

- Fixed UnicodeError in CMF actions with non-ascii in title or description
  after migration from Plone pre-3.0. This closes
  http://dev.plone.org/plone/ticket/7133.
  [hannosch]

- In inline selection widgets (with KSS) display the label, as
  otherwise you only see identical radio buttons without text,
  giving you no clue of what you are selecting.  Fixes #7243
  [maurits]

- When changing the ownership of an object the new owner may now
  also be in the top level acl_users folder in the Zope root.
  This fixes http://dev.plone.org/plone/ticket/5730
  [maurits]

- Now displaying a error status message instead of a traceback
  when trying to cut a locked item.  This closes
  http://dev.plone.org/plone/ticket/7711
  [maurits]

- Removed dependencies checking code, we have setuptools for this.
  [hannosch]

- Avoid events to be shown in the previous and upcoming events collections
  at the same time. This closes http://dev.plone.org/plone/ticket/7790.
  [hannosch]

- Updated table of contents javascript to calculate how much left margin
  will be needed for lists larger than 9 to show properly. This closes
  http://dev.plone.org/plone/ticket/8366
  [dunlapm]

- Updated folder_listing and folder_summary_view to not assume that events
  will have a location defined. This closes
  http://dev.plone.org/plone/ticket/8358
  [dunlapm]

- In discusssion_reply_form.cpt not only redefine the 'here'
  variable but also 'context', which is needed for rendering the
  main macro of the item under discussion.  A reply to a reply
  would give an error when the template for the item under
  discussion was using 'context' instead of 'here'.
  See http://comments.gmane.org/gmane.comp.web.zope.plone.devel/19657
  (merged from trunk r22018)
  [maurits]

- Modified getSectionFromURL to return an empty string instead of None
  which prevents main_template assigning the nonsense CSS class of "None".
  This closes http://dev.plone.org/plone/ticket/8283.
  [dunlapm]

- Added 'pwreset_finish' to the ignore_came_from list in login_next.cpy.
  Back-ported from r21501. This closes
  http://dev.plone.org/plone/ticket/5548 and
  http://dev.plone.org/plone/ticket/8356.
  [hannosch/dunlapm]

- Corrected behavior in the URL tool to more intelligently handle relative
  URLs in isURLInPortal. The new functionality requires the current context
  to be passed in to figure out urls beginning with any number of the '../'
  sequence. The current context is optional and the tool will default to the
  old behavior if it is not present. Tests have been added to deomonstrate
  the new behavior. This closes http://dev.plone.org/plone/ticket/6691
  [dunlapm]

- Corrected transaction note in renameObjectsByPaths.
  [hannosch]

- Fixed an inconsistent description in the navigation control panel.
  This closes http://dev.plone.org/plone/ticket/8286.
  [hannosch]

- Fixed prefs_groups_overview.cpt so that hitting enter in the search
  box does not add a new group. Closes
  http://dev.plone.org/plone/ticket/6187
  thanks to claytron for the patch
  [calvinhp]

- Fixed login_failed.cpt to not show portlets.  Closes
  http://dev.plone.org/plone/ticket/8306
  [davisagli]

- Fixed color for links of Schematas' titles in edit forms.
  Closes http://dev.plone.org/plone/ticket/6778
  [spliter]

- Fixed thumbnail view for IE6 for cases when any photoAlbumEntry
  has too long title. Fixes http://dev.plone.org/plone/ticket/7378
  [spliter]

- Added property which controls the availability of inline editing.
  [fschulze]

- Hide #portal-languageselector on printed page. This fixes
  http://dev.plone.org/plone/ticket/8299
  [naro]

- Fixed folder_listing, folder_summary_view, and folder_tabular_view
  templates to support batching for collections in addition to normal
  folders.  This fixes http://dev.plone.org/plone/ticket/8121.
  [davisagli]

- Allowing only positive integers (1 or greater) for field max_items in
  synPropertiesForm.cpt. This fixes http://dev.plone.org/plone/ticket/8279.
  [rsantos]

- Always setting sort_order in search_rss.pt, even when sort_on is not
  supplied. This fixes http://dev.plone.org/plone/ticket/7908.
  [rsantos]

- Adjusted AddMoveAndDeleteDocument test to not rely on the 'my folder'
  action anymore and removed troubled tests for the old and deprecated
  calendar portlet.
  [hannosch]

- Making sure that the draggable elements are in invisibles.css, so they
  work independent of which theme you have installed. This fixes
  http://dev.plone.org/plone/ticket/7773.
  [limi]

- Fixed display of LiveSearch when it's rendered in the left column.
  This fixes http://dev.plone.org/plone/ticket/6903
  [limi]

- Overhauled the hCard/hCalendar support on the Events page, this fixes
  http://dev.plone.org/plone/ticket/6888 and
  http://dev.plone.org/plone/ticket/6889, and refs
  http://dev.plone.org/plone/ticket/6333 and
  http://dev.plone.org/plone/ticket/#6708
  [limi]

  - Fixed hCard syntax to be able to include email address.

  - Fixed spamProtect.py script to be able to accept optional arguments
    for HTML classes/ids and render them in the returned tag.

  - Inserted the fn/url classes on the mailto link now that it is
    supported.

  - Made the name render with a mailto link now that spamProtect supports
    it (it already supported this for a while, we just never used it).

  - dtstart/dtend classes were being overwritten by KSS class definitions,
    so the hCalendar event tags were never rendered, breaking our
    hCalendar support. Fixed.

  - When there is no fullname, show email address. This would turn out
    blank earlier. Fixed.

  - The date *has* to be supplied inside an abbr tag for most parsers.
    Fixed.


- Removed the mystuff action from the default profile. It was accidentally
  left in place but correctly removed during upgrade. This closes
  http://dev.plone.org/plone/ticket/7903.
  [hannosch]

- Fixed upgrade bug that caused the 'Home' portal tab to disappear when
  upgrading from Plone 2.5. This closes
  http://dev.plone.org/plone/ticket/7902.
  [hannosch]

- Fixed prefs_group_details.pt to not error when creating a new group with
  empty lines property. This closes http://dev.plone.org/plone/ticket/8036
  [dunlapm]

- Fixed default_error_message not respecting Allow Anonymous to View About
  information. This closes http://dev.plone.org/plone/ticket/7685
  [dunlapm]

- Expanded the difftool migration profile setup to configure the diffs
  for all types, since otherwise migrated sites will not get any diffs
  configured except for folders.
  [hannosch]

- Moved GS import step difftool registration to the CMFDiffTool product.
  [hannosch]

- Fixed formUnload.js for file and hidden fields. This closes
  http://dev.plone.org/plone/ticket/5121
  [mj, duncan]

- Refactored the calendar_form.js code, fixing several problems, and
  improving overall usability and maintainability. This closes
  http://dev.plone.org/plone/ticket/5623,
  http://dev.plone.org/plone/ticket/6612,
  http://dev.plone.org/plone/ticket/7505 and
  http://dev.plone.org/plone/ticket/8020
  [mj]

- Upgraded jquery to 1.2.6.
  [mj]

- Make sure that activateCollapsibles can be called more than once
  on a page (e.g. when you ajax stuff into the page that contain collapsibles)
  [dannyb, mj]


3.1.4 - July 24, 2008
---------------------

- No changes.
  [wichert]


3.1.3 - July 8, 2008
--------------------

- Adjusted deprecation warnings to point to Plone 4.0 instead of Plone 3.5
  since we changed the version numbering again.
  [hannosch]

- Fix error in display of atct_album_view for folders not containing
  Images. Closes http://dev.plone.org/plone/ticket/8212.
  [esteele]

- Modify @@plone/prepareObjectTabs to honour the order within the
  sort_first parameter.
  [wichert]

- Correct calculation of the redirect URL used when redirecting from
  a discussion item to the content view.
  [wichert]

- Add CSRF protection test for managing server secrets via the Plone
  session plugin for PAS. Also see http://dev.plone.org/plone/ticket/8176
  [witsch]


3.1.2 - June 3, 2008
--------------------

- Apply fix for http://dev.plone.org/plone/ticket/8159. This fixes
  the event listing of future events. Fix from Sergey Volobuev.
  [seletz]

- Update CSRF protection tests and add authenticator token to "change
  ownership" form. This fixes http://dev.plone.org/plone/ticket/8131
  [witsch]

- Fix currently selected portal_tab when some actions are linking to
  external urls. This fixes http://dev.plone.org/plone/ticket/7155.
  [laz]

- Updated add-on installation screen to sort by title instead of id.
  This closes http://dev.plone.org/plone/ticket/8012.
  [hannosch]

- Sarissa.js is also used by KSS; load it for non-anon users as well (like
  the KSS libraries). This closes http://dev.plone.org/plone/ticket/8141
  [mj]


3.1.1 - released April 28, 2008
-------------------------------

- Fix CSRF protection for changing the workflow state through the
  "advanced" publishing process form and via the "change state"
  button of the "folder contents" view. This fixes
  http://dev.plone.org/plone/ticket/8066
  [witsch]

- Fix CSRF protection for adding a user to a group via the "group members"
  tab. Fixes http://dev.plone.org/plone/ticket/8024
  [witsch]


3.1 - released April 22, 2008
-----------------------------

- Added protection against CSRF attacks to various methods and
  forms (see `tests/csrf.txt`).
  [witsch]

- Fixed typo in ploneKss.css
  [malthe]

- Remove all invalid leading spaces in hrefs.
  [wichert]

- Mime type text/x-html-captioned was added to the forbidden list of types.
  This closes http://dev.plone.org/plone/ticket/7943.
  [hannosch, duncan]


3.1-rc1 - released March 28, 2008
---------------------------------

- Adjust 2.5.x - 3.0-alpha1 migration so portlets are not added twice
  for migrated sites.
  [wichert]

- Added missing i18n markup to portlets.xml file. This refs
  http://dev.plone.org/plone/ticket/7768.
  [hannosch]

- Fixed out-of-sync calendar days and weekdays in the calendar portlet.
  This closes http://dev.plone.org/plone/ticket/7931.
  [hannosch]

- Include the short product description for extension profile based
  add-ons in the add-ons control panel. This gives non-Zope2 products a
  way to provide more information, as their readme.txt cannot be found.
  [hannosch]

- Updated list of non-installable products, now that quickinstaller
  recognizes non-Zope2-products.
  [hannosch]

- Teach folder_listing to now try batching when dealing with a
  Topic/Collection. This fixes http://dev.plone.org/plone/ticket/7937
  [wichert]

- Correct styling of ul elements in portlets. This corrects styling of
  the language portlet and is very common in custom sites.
  [wichert]


3.1-beta1 - released March 9, 2008
----------------------------------

- Added setup code and migration to ensure that the "Sharing" page action
  is protected by the correct permission.
  http://dev.plone.org/plone/ticket/7652
  [optilude]

- Fix batching on standard folder listings. Thanks to erral for the patch!
  http://dev.plone.org/plone/ticket/7508
  http://dev.plone.org/plone/ticket/6091
  [optilude]

- Fix folder_summary_view display of Link objects.
  http://dev.plone.org/plone/ticket/7509
  [optilude]

- PLIP213: Moved RSS link macro to a viewlet in plone.app.layout.links.
  [fschulze]

- PLIP217: Use adaptation to determine workflow chain.
  [alecm]

- PLIP208: Use borg.localrole for local role assignment via adaptation.
  [alecm]

- PLIP203: Move portlet assignment setup on site creation to use the new
  GenericSetup syntax.

- PLIP202: Add formlib inline validation and editing support.
  [optilude]

- PLIP184: Install plone.portlet.static and plone.portlet.collection
  [optilude]

- prefs_install_products_form.pt directed users to add new add-on products
  to $INSTANCE_HOME/Products. Bad advice for buildout users. Now, it
  will look for "/parts/" (or "\parts\") in path and give buildout
  instructions if found.
  [smcmahon]


- Remove double registered GenericSetup steps from the persistent registry.
  [wichert]

- Teach the migration tool to correctly handle unicode log messages.
  [wichert]

- Add a new dependencies GenericSetup profile to CMFPlone which is
  loaded at the end of Plone site creation. This allows use of
  GenericSetup profile dependencies for Plone itself.
  [wichert]

- PLIP224: Install plone.app.protect
  [wichert]

- PLIP220: Install plone.browserlayer
  [wichert]

- PLIPs 205 and 218: Allow registering portlet types to multiple portlet
  manager interfaces, require portlet types to be explicitly registered
  for portlet manager interfaces, enable modifying registrations through
  GenericSetup, and restrict most default Plone portlet types to left/
  right/dashboard columns.
  [sirgarr]

- PLIP207: Allow custom portlet managers, i.e., allow specifying an
  alternative portlet manager class through GenericSetup.
  [sirgarr]


3.0.7
=====

- Don't test the internal policy of the normalization logic. This is
  covered by the tests in plone.i18n.
  [hannosch]


3.0.6 - released February 15, 2008
----------------------------------

- Make @@plone_lock_info not required for object_cut, object_delete and
  delete_confirmation scripts (not all content is lockable.)
  [ldr]

- Five.testbrowser tests could not log in via the login_form.
  [stefan]


3.0.5 - released January 5, 2008
--------------------------------

- Fixed issues when non-savepoint supporting connections are
  involved in a folder_delete, folder_publish, or folder_rename.
  [alecm]

- Remove utility registration for portal_quickinstall and portal_setup:
  they may run arbitrary code that relies on having a full acquisition
  chain including a request container.
  [wichert]

- Backported changeset 18612 and 18615 from trunk. This fixes some
  deprecation warnings.
  [hannosch]

- If you are using the fullscreenmode.js script, you can now pass in a
  'minimal=1' argument in the URL to make a page start out in the minimal
  mode.
  [fschulze] [limi]

- Hiding page history, page navigation, and busy icon (spinner) in print.css
  Related to http://dev.plone.org/plone/ticket/7433 and
  http://dev.plone.org/plone/ticket/7402
  [siebo]

- Removed 'Groups' dropdown from Users tab, as it did not and could not
  work.
  Fixes http://dev.plone.org/plone/ticket/7260
  [derek_richardson]

3.0.4 - released December 7, 2007
---------------------------------

- Added migration to enable workaround for CMFEditions large file
  handling issue.
  Related to http://dev.plone.org/plone/ticket/7223
  [alecm]

- In livesearch reply, html quote the description to disable the
  inclusion of arbitrary html and executing arbitrary javascript
  when the search result is displayed.
  Fixes http://dev.plone.org/plone/ticket/7439
  [ree]

- GenericSetup profile ids now have to have a prefix for certain calls.
  Fixes http://dev.plone.org/plone/ticket/7435
  [witsch]

- Moved folder_rename logic into PloneTool and added
  savepoint+rollback there as well.  Additionally, folder_rename
  now requires POST requests.
  [alecm]

- Moved most folder_publish and folder_delete logic into PloneTool
  methods.  Added savepoints and rollbacks for folder publish and
  delete actions, so that partial deletions/transitions are not
  committed.  Made folder_publish require POST. Thanks to rossp
  for finding this.
  [alecm]

- Undeprecated fullscreen.js - it still exists in the actions, but is
  turned off by default. It shouldn't have been moved to the
  plone_deprecated skin layer. If you want to use it, you'll need to
  add it to the JS registry manually, though - as we don't include it
  in the default JS setup, since it's not in use by default.
  [limi]

- Remove duplicate calling of customization macros
  in personalize_form.cpt
  Fixes http://dev.plone.org/plone/ticket/7359
  [seletz on trunk (4.0), maurits on 3.0]

- Complete support for show_ymd to the calendar widget template. This makes
  it possible to create time-only widgets.
  [wichert]

- Allow non ascii characters in webstats_js code.
  Fixes http://dev.plone.org/plone/ticket/7359
  [naro]

- No longer require a _catalog property on portal_catalog for migration.
  This avoids migration errors on sites with e.g. QueueCatalog installed.
  [alecm]

- Added diff tool entry for Folder type.
  Fixes http://dev.plone.org/plone/ticket/7253
  [alecm]

- Fix for user titles on ownership_form, which were showing the
  current member title instead of prospective owners.  Thanks to
  younga for the fix.
  Fixes http://dev.plone.org/plone/ticket/7286
  [alecm]

- Fix to the Table of Contents code generation, so it doesn't produce
  invalid HTML even if you feed it an invalid nesting structure.
  Fixes http://dev.plone.org/plone/ticket/6930
  Thanks to davisagli for the fix.
  [limi]

- Avoid the unlock handler to act if we are submitting with ok button.
  (Fixes ConflictError-s in case of an object is created without
  the portal factory.)
  [ree]

- Fix TypeError when an anonymous user locks content.  Fixes
  http://dev.plone.org/plone/ticket/7246
  [maurits]

- Index interface.__identifier__ instead of interfaceToName(interface),
  a 5x speed improvement when reindexing.
  [mj]

3.0.3 - released November 9, 2007
---------------------------------

- Allowed the abbr, acronym, var, dfn, samp, address, bdo, thead, tfoot,
  col, and colgroup tags by default, since they are harmless, valid XHTML
  and shouldn't be filtered. Fixes:
  http://dev.plone.org/plone/ticket/6712 and
  http://dev.plone.org/plone/ticket/7251
  No migration performed, as we don't want to adjust custom filtering -
  if you want to update this in your existing site, go to the HTML
  Filtering control panel and remove these from being filtered.
  [limi]


3.0.2 - released October 10, 2007
---------------------------------

- Give 'Modify portal content' permission to the Owner role by default.
  This allows sane use of workflow-less content types. Fixes
  http://dev.plone.org/plone/ticket/7180
  [wichert]

- Modify form_tabbing.js to not touch the edit form if there's no
  fieldsets.
  [nouri]

- Set the media for ploneKss.css to screen so it can be merged with the
  other CSS files.
  [wichert]

- Add the language control panel when migration from previous Plone
  versions.
  [wichert]

- Fixed missing i18n markup in folder_constraintypes_form for portal types
  translation. This closes http://dev.plone.org/plone/ticket/7067.
  [hannosch, naro]

- Add migration to set the default GS profile when upgrading from 2.1.
  [alecm]

- Use a button/script combo for product reinstall from the control
  panel.  http://dev.plone.org/plone/ticket/6457
  [alecm]

- Remove silly root check from stripGRUFLocalRolePrefix script to
  fix migration bug. http://dev.plone.org/plone/ticket/5817
  [alecm]

- Made Plone use 1/10th of the memory on file uploads. Details in
  http://dev.plone.org/plone/ticket/7027
  (also backported to Plone 2.5.x)
  [zegor]

- Reverted addition of the GenericSetup import and export steps from
  PloneLanguageTool.
  [hannosch, wichert]

3.0.1 - released September 13, 2007
-----------------------------------

- Made default_error_message more robust when the NotFound path traverses
  a view.
  [ldr]

- Let the Editor role get 'Delete objects' permission, making it easier
  to delegate content management in a folder.
  http://dev.plone.org/plone/ticket/7078

- Added a wide range of proxy roles to check_id script, should allow it to
  work with all but the most unusual workflows.  Eventually this should
  be converted to trusted code.
  http://dev.plone.org/plone/ticket/6999
  [alecm]

- Fixed all the default view templates to use Archetypes' view mode for
  the widgets instead of using a special KSS template. This means that
  it's now very easy to add inline editing to your custom types, look
  at document_view.pt for an example. You just call the widget in view
  mode, and Plone takes care of the rest.
  http://dev.plone.org/plone/ticket/6705
  [limi]

- Added migration for view customization container and utility.
  [witsch]

- NuPlone didn't set the background color explicitly on the body element,
  fixed.
  [limi]

- Adjusted some deprecation warnings to a later Plone version, as we
  haven't removed all usage of the underlying functions from Plone itself.
  [hannosch]

3.0 - released August 17, 2007
------------------------------

- Remove usage of login.js and Deprecate it.
  [ree, wichert]

- Update migration code for final release.
  [wichert]

- Remove keywords/category listing from document byline and
  instead render it as a viewlet right below that.
  [maurits]

- Make workflow history visible again, as viewlet just below the
  body of the content.  Fixes
  http://dev.plone.org/plone/ticket/6933
  [maurits]

- Let the "manage portlets" fallback link (for when no columns are shown)
  use the canonical object (i.e. object without default view), in the same
  way that the column would have done. Fixes
  http://dev.plone.org/plone/ticket/6927
  [optilude]

- Sort the configlets in the control panel by their translated title
  instead of their English title.
  [hannosch]

- Fixed erroneous message when publishing multiple items and a subfolder
  with no items was present. Also synced status message with the
  content_status_modify script, so only one message is shown.
  This closes http://dev.plone.org/plone/ticket/6553.
  [hannosch]

- Fixed a few status messages to work with content item titles with
  non-ascii characters in them.
  [hannosch]

- Plone 3.0 has an ID "content" that only includes the actual content,
  not everything in the content well. Adjusted the getContentArea()
  method in register_function.js to prefer this if it's present.
  This fixes http://dev.plone.org/plone/ticket/5701
  [limi]

- Fixed incorrect redirect when pressing the cancel button on the
  sharing tab.  For Files it would cause you to download the file.
  This fixes http://dev.plone.org/plone/ticket/6874
  Fixed in plone.app.workflow.
  [maurits]

- Fix incorrect use of getActionById that caused an error when
  sending someone a link to an item in the site.  This fixes
  http://dev.plone.org/plone/ticket/6857
  [maurits]

- The wiki syntax support now supports both the [[link]] and ((link))
  syntax variations by default. Removed the preference for selecting
  between them, since it no longer does anything.
  [limi]

- Adding a mini-login form to the login failure screen. This fixes
  http://dev.plone.org/plone/ticket/6776
  [limi]

- Since the CSS isn't recalculated if you switch to https mid-flight,
  we need to add https version of portal_url to the blacklist to avoid
  getting the lock icon on local links. This fixes:
  http://dev.plone.org/plone/ticket/6821
  http://dev.plone.org/plone/ticket/6767
  [limi]

- Fixed permissions for iterate check-in/check-out so that non-manager
  users can use it. Fixes http://dev.plone.org/plone/ticket/6645
  [optilude]

- Corrected broken Javascript regular expression that caused almost
  arbitrary stuff in the query string to cause 'searchterm'-highlighting.
  Thanks to Claytron for patch.
  Fixes
  http://dev.plone.org/plone/ticket/6824
  http://dev.plone.org/plone/ticket/6811
  [elvix]

- Reformatted the workflow descriptions in order to prevent insane amount
  of whitespace to show up in the translations.
  [hannosch]

- Added i18n markup to the workflow descriptions in GenericSetup profiles.
  [hannosch]

- Remapping the "(Default)" workflow to No Workflow didn't work.
  Fixes http://dev.plone.org/plone/ticket/6818
  [optilude]

- Remapping to "No Workflow" resulted in an error, fixed. Thanks to
  rsantos for the patch. Fixes http://dev.plone.org/plone/ticket/6819
  [limi]

- Author profile template was showing left/right portlets, removed these.
  [limi]

- Removed httpresponse patch, which is obsolete with Zope 2.10.4 which we
  do require now.
  [hannosch]

3.0-rc2 - released July 27, 2007
--------------------------------

- Added a description to the no-workflow information in the types
  control panel. This fixes http://dev.plone.org/plone/ticket/6812
  [wichert]

- Added in markup for the IDs #contentTopLeft, #contentTopRight,
  #contentBottomLeft, #contentBottomRight to allow rounded corners on the
  content well using the same technique as the portlets.
  [limi]

- Updated componentregisty.xml to new style. As the object handler only
  supports registering objects in the site itself now, we can remove all
  the slashes.
  [hannosch]

- Updated the migration tool to use the "upgrade" terminology, to be
  consistent with the recent documentation. Also removed useless tab,
  all information is on one screen now.
  [limi]

- Move login and logout-handling code into the membership tool and
  add sending of events when a user logs in or logs out. For Plone 4.0
  we can move most of the code into event handlers.
  [wichert]

- Harmonized the link classes for wiki links with the Plone standard,
  made pages that haven't been created yet red, made the entire link
  clickable, made the "+" superscript.
  [limi]

- The protocol-specific links should only be applied inside the content
  area.
  [limi]

- Fixed inline editing for dates in event_view
  [spliter]

- Fullscreen view for images has a title of it's parent now
  [spliter]

3.0-rc1 - released July 13, 2007
--------------------------------

- CMF has renamed getToolByInterfaceName to getUtilityByInterfaceName.
  Update our scripts accordingly.
  [wichert]

- validate_email is stored on the portal root, not in site_properties.
  Make all scripts and templates aware of that.
  [wichert]

- No longer do portlet and action calculations on error pages.
  This will make them less resource intensive, and less likely to
  throw their own errors (which resulted in an XSS issue).
  Additionally, this means that there is now a means for any
  template to avoid portlet and action processing as needed.
  [alecm]

- Remove hard-to-cache recent portlet from the default front page. It's
  on the default dashboard.
  [optilude]

- Changed the behaviour of the "Allow comments" to be a checkbox instead
  of having three settings. It now respects the global setting unless you
  made a manual change on that particular document.
  This closes http://dev.plone.org/plone/ticket/5977
  [hannosch, limi]

- Moved the login.js script to only trigger on the login_form page, since
  that's where the login portlet posts to anyway. Carrying it around on
  every page doesn't make sense.
  [limi]

- The mark_special_links javascript is no longer hooked up, since we use
  CSS to do the various protocol-specific markers now.
  It's *not* removed from existing sites that use it, but new sites
  will not have it enabled. The CSS approach works in all modern browsers,
  but not Internet Explorer 6. It works fine in IE7, however.
  If you are upgrading from an earlier Plone release, you
  might want to remove the script manually to reduce page weight.
  [limi]

- Moved several javascripts to be rendered for logged-in users only to
  reduce the weight of the anonymous page load.
  [limi]

- If we failed to send the user registration email but the user selected
  his own password to not remove the newly created user but just warn
  him that the email failed.
  [wichert]

- Do not allow user registration if the site is configured to email
  password but no mail configuration has been set.
  [wichert]

- Escape userids and groupnames in all templates so we can handle ids with
  unfriendly characters.
  [wichert]

- Cleanup handling of userids and loginnames: consistently use userids to
  key all user information.
  [wichert]

- Disable the mobile style sheet by default, since very few people use it,
  and we're planning to re-work this in 4.0 anyway. If you need it, simply
  turn it back on in portal_css.
  [limi]

- Deprecated presentation.css since the presentation code uses the
  dedicated S5 CSS files now.
  This closes http://dev.plone.org/plone/ticket/6304
  [limi]

- Images and Files no longer have a workflow in the new default setup,
  making them always visible.
  This closes http://dev.plone.org/plone/ticket/6740
  [limi]

- Workflow states now have a description.
  This closes http://dev.plone.org/plone/ticket/6498
  [limi, hannosch]

- Remove the community workflow and re-title the Plone workflow to
  "Community workflow".
  [wichert]

- In the simple publication workflow, the author can now edit a published
  item. He cannot edit it while it is pending, though.
  [limi]

- Blacklist the 'layout' id to prevent conflicts with the layout property
  on dynamic view capable content. This fixes
  http://dev.plone.org/plone/ticket/5970
  [wichert]

- Allow form tabbing using other elements than forms. This allows tabbing
  between multiple forms, which is needed by the content rules config
  panel.
  [wichert]

- Factored most of the "add menu" functionality out of
  plone.app.contentmenu into plone.app.content.browser.folderfactories.
  This contains a view which powers the folder_factories view. The old
  template-based version is moved to plone_deprecated and is renamed
  old_folder_factories. Closes http://dev.plone.org/plone/ticket/6370.
  [optilude]

- Made the home link on the login success page link to the navigation root
  rather than always linking to the site root. Fixes
  http://dev.plone.org/plone/ticket/6001.
  [optilude]

- Made all portlet management functions use explicit referer URLs, rather
  than relying on HTTP_REFERER. Hopefully this fixes problems with IE7
  not passing this value properly. Should fix
  http://dev.plone.org/plone/ticket/6395 and
  http://dev.plone.org/plone/ticket/6641.
  [optilude]

- Added an event handler to create a default dashboard when a new user
  is created. This can be overridden using an adapter from IBasicUser to
  IDefaultDashboard from plone.app.portlets.
  Closes most of http://dev.plone.org/plone/ticket/6198.
  [optilude]

- Added a message to the dashboard when it is empty, instructing users to
  add some portlets.
  Refers to http://dev.plone.org/plone/ticket/6198.
  [optilude]

- Made the cut and delete items in the 'actions' menu fail with a status
  message explaining the error, rather than an exception, when the context
  is locked.
  [optilude]

- Ensured that the 'rules' tab is not displayed if content rules are
  disabled globally. Fixes http://dev.plone.org/plone/ticket/6449.
  [optilude]

- Show the locked icon to any user (including the one who holds the lock)
  so long as they would normally have the "Modify portal content"
  permission. This makes it easier to realise when you inadvertently
  locked an object.
  [optilude]

- Fixed _at_creation_flag on initial content. This closes
  http://dev.plone.org/plone/ticket/6642.
  [hannosch]

- Remove the properties action from all FTIs.
  [wichert]

- Corrected status messages emitted by the join form and personalize
  validators. This closes http://dev.plone.org/plone/ticket/6518.
  [hannosch, wichert]

- Unregister tools which are no longer action providers. This fixes
  http://dev.plone.org/plone/ticket/6730
  [wichert]

- Added tests for sending mails via the contact form with Unicode input.
  The actual bug was fixed in SecureMailHost. This closes
  http://dev.plone.org/plone/ticket/6574.
  [hannosch]

- Added migration to the new five.localsitemanager lookup class.
  [hannosch]

- Added proper byline on search results, optimized layout.
  [limi]

- Adding support for the rel="tag" microformat.
  This closes http://dev.plone.org/plone/ticket/5351
  [limi]

- Separate the kss resources to a development and production version,
  and change portal_javascript entries to switch to the new resources.
  Modes can be switched by setting portal_javascript to debug mode, or
  by visiting the view @@kss_devel_mode/ui (this works with client side
  cookies, and thus enables changing the development mode of kss
  without touching the server).
  [ree]

- Use the PlonePAS way of setting member properties
  [wichert]

- Removed utility registrations for tools that are not utilities anymore.
  [hannosch, wichert]

- Updated the factory and migration_util code to use the new GenericSetup
  methods for directly loading profiles, without setting the context.
  [hannosch]

- Small i18n markup fix in the control panel overview. Dynamic content
  inside a message has to be quoted by using i18n:name.
  [hannosch]

- The persistent type information of the Topic type was not updated to its
  new name Collection. This closes http://dev.plone.org/plone/ticket/6546.
  [hannosch]

- Reformatted the migration registrations for less excessive whitespace use.
  [hannosch]

- Added migration registrations for the 2.5.3 rc1 and final releases.
  Corrected the history. This closes
  http://dev.plone.org/plone/ticket/6659.
  [hannosch]

- Added the selected year to the options in the calendar date picker box
  if it was not in the available range, so you can always keep the year.
  This closes http://dev.plone.org/plone/ticket/5279.
  [hannosch]

- No longer migrate the deprecated related and language portlets to
  classic portlet assignments in the portal root. This closes
  http://dev.plone.org/plone/ticket/6545.
  [hannosch]

- Made the user preference for which editor to use translatable. This
  closes http://dev.plone.org/plone/ticket/6386.
  [hannosch]

- Consistently bicapitalized 'JavaScript'. This closes
  http://dev.plone.org/plone/ticket/6636.
  [hannosch]

- Fixed explanation on the navigation control panel. This closes
  http://dev.plone.org/plone/ticket/6643.
  [hannosch]

- Updated the language control panel to a new formlib-based version which
  shows all the language names localized to your language.
  This refs http://dev.plone.org/plone/ticket/5442.
  [hannosch]

- Added migration to move the kupu (core) and CMFPlacefulWorkflow (add-on)
  control panels to the right categories. This closes
  http://dev.plone.org/plone/ticket/6547.
  [hannosch]

- In plone.app.viewletmanager GenericSetup handler: Added support for
  'based-on' and 'make-default' parameters in <order /> and <hidden />
  nodes, value for 'skinname' can be "*" (means all). Added support for
  'insert-before', 'insert-after' (value can be "*") and 'remove'
  parameters in <viewlet /> node. Viewlets ordering and hiding are now
  additive. This closes http://dev.plone.org/plone/ticket/6649.
  [davconvent]

- Made 'prefs_user_details' pull its form from 'personalize_form' to
  minimize duplicated code. If you have customized any of these templates,
  you should probably revisit them and update your templates accordingly.
  [limi]

- Moved footer.pt, colophon.pt and global_contentviews.pt to viewlets,
  found in plone.app.layout.viewlets. The original templates are now in
  the plone_deprecated layer.
  [optilude]

- Users aren't invited to contact the site admin anymore if mail settings
  are not set. This closes http://dev.plone.org/plone/ticket/6322.
  [hannosch]

- Changed the global section (tab) navigation so that it shows non-
  folderish items as well as folderis ones by default (for migrated
  the sites, the default is not to display them). Also changed the
  navigation tree so that it start at level 1, not the site root by
  default (again does not affect migrated sites). This makes it easier to
  have a separate front page, and lets the tabs act as first-order
  navigation with the navtree acting as second-order-and-below.
  [optilude, limi]

- Added a persistent zope.app.cache based RAMCache, which is used for
  caching the portlets by default. Configuration is available via
  http://portal/@@ramcache-controlpanel.
  [hannosch]

- Allow user ids that are substrings of existing user ids.  This
  fixes http://dev.plone.org/plone/ticket/6396
  [nouri]

- Fix `RegistrationTool.mailPassword` by passing the results of
  `reset_tool.requestReset` to it, instead of having the template
  call the tool's function.  Also take care about encoding, since
  the template returns unicode now.  This makes e-mailing
  forgotten passwords work again, and fixes
  http://dev.plone.org/plone/ticket/6614
  [nouri]

- Added an opt-out for multi-submit protection. Add a class to the input
  tag called "allowMultiSubmit".
  [optilude, ree, fschulze]

- Adjusted our RegistrationTool's mailPassword method not to use the
  method from the base tool anymore, as that has changed in incompatible
  ways.
  Reverted the method to use the same logic as in CMF 1.6. This refs
  http://dev.plone.org/plone/ticket/6614.
  [hannosch]

- Corrected inconsistent slashing of URLs in folder listings, fixes
  http://dev.plone.org/plone/ticket/4912

- Fixed migration from Plone < 2.5. The portal_setup tool needs to be
  installed before installing CMFPlacefulWorkflow now. This closes
  http://dev.plone.org/plone/ticket/6610.
  [hannosch]

- Added ZPT-like i18n markup to GenericSetup profiles, which is used for
  automatic message extraction by i18ndude.
  [hannosch]

- Cleaned and speed up ulocalized_time functions. Added request to the
  method signature which was implicitly acquired so far. Now you can
  optionally provide it directly.
  [hannosch]

- Corrected spelling error in validate_folder_constraintypes.vpy. This
  closes http://dev.plone.org/plone/ticket/6591.
  [hannosch]

- Fixed duplicate class definitions in some templates.
  [hannosch]

- Fixed lots of small i18n markup errors. Mostly using different message
  ids for messages whose text has changed significantly.
  [hannosch]

- Link to the users dashboard from password_form and personalize_form,
  instead of to the plone_memberprefs_panel.
  [hannosch]

3.0-beta3 - released May 5, 2007
--------------------------------

- Allowed any non-structural folders and non-folderish items be eligible
  as default view types. Structural folders can still be listed if they
  are added to the default_page_types property. This closes
  http://dev.plone.org/plone/ticket/6118
  [optilude]

- Gave the Editor role a few additional permissions:
  "Modify view template", "Request review" and "Modify properties". This
  closes http://dev.plone.org/plone/ticket/6530
  [optilude]

- Moved sharing action to a global action and removed from standard
  types. This closes http://dev.plone.org/plone/ticket/6335
  [optilude]

- Fixed migration code for CMFEditions. This closes
  http://dev.plone.org/plone/ticket/6491
  [hannosch]

- Fixed member_search_results to work for users without a fullname.
  [hannosch]

- Added plone.app.viewletmanager. This allows you to hide and order the
  viewlets per skin via a GenericSetup profile.

3.0-beta2 - released May 2, 2007
--------------------------------

- Extended support for creation of translated initial content to include
  all titles and descriptions of all initial content.
  [hannosch]

- Add getChainFor method in WorkflowTool from CMFPlacefulWorkflow
  monkey-patch and disable this one.
  [encolpe]

- Hide CMFPlone on the add-on product installation control panel.
  This fixes http://dev.plone.org/plone/ticket/6513.
  [hannosch]

- Fix bad links between templates prefs_users_overview, prefs_user_details
  and prefs_user_membership (remove starting space and force portal_url)
  [encolpe]

- Separated the Editor role into Editor and Contributor, the latter with
  responsibility for adding content. This is necessary in order to support
  the (most common?) use case of wanting to have a folder in which people
  can add content, but not edit the folder itself!
  [optilude]

- Moved global_logo, global_pathbar, global_personalbar, global_searchbox,
  global_sections and global_siteactions to viewlets in plone.app.layout.
  [fschulze]

- Add POST-only protections to security critical methods (see
  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-0240).
  [mj, bloodbare, alecm]

- Switched to the simple_publication_workflow as the default workflow.
  Note that the tests still assume plone_workflow is the default (see
  the previous change message below).
  [optilude]

- Made an extension profile for the default Plone test fixture in
  profiles/testfixture. For now, this explicitly sets the test fixture
  workflow. This profile should be used with care - deviate too far from
  the base profile and tests become meaningless! However, some deviation
  may be inevitable in order to have sane and predictable tests.
  [optilude]

- Deprecate Products.CMFPlone.utils.BrowserView. Its users should use
  Products.Five.BrowserView directly.
  [wichert]

- Removed presentation.css, as the presentation mode has moved to use
  the S5 presentation mode.
  [limi]

- Cleaned up the ID mess around which ID/class that wraps the actual
  content (without the UI elements in the content well). The official
  approach is now to use #content for the actual content, and to use
  #portal-column-content for the entire content region. Also made it
  possible to get rid of some !important statements.
  If you have CSS that depends on either of these two selectors, you might
  want to make sure that the output is still as expected. It should work
  the same way in most cases, but since the scope is narrower for #content
  now, you might need to update your styles (and main_template needs to
  be updated too, if you have customized that).
  Fixes http://dev.plone.org/plone/ticket/6465
  [limi]

- Let users with the Editor local role add content in folders. Note that
  this will only work for third party content types and custom workflows
  if  they either use one of the standard "add content" permissions or
  explicitly give Editor the Add portal content role. Fixes
  http://dev.plone.org/plone/ticket/6265
  [optilude]

- Deprecated ploneifyActions.py and moved the functionality to the
  @@plone view. As part of this, removed the use_folder_tabs property.
  All structural folders now use folder tabs; this property pre-dates
  the concept of non-structural folders.
  [optilude]

- Reindex security recursively after group name update in
  stripGRUFLocalRolePrefix. Fixes
  http://dev.plone.org/plone/ticket/5817
  [alecm]

- Add back user skin cookie deletion on logout.  Fixes
  http://dev.plone.org/plone/ticket/2563
  [alecm]

- Added visual styles and updated markup for the new "Info", "Warning" and
  "Error" status message levels.
  [limi]

- Made the error page much friendlier, it essentially just prints a log
  entry number now and explains that the error has been logged. If you are
  logged in as an administrator, you have access to the full error log.
  This fixes http://dev.plone.org/plone/ticket/6277
  [limi]

- Ensured that templates missing the initial h1 class
  "documentFirstHeading" got it applied, since it makes a difference with
  the header styling. If you see additional space above your headlines in
  your own products or add-on products, please insert this class.
  It would have been nice if IE supported :first-child selectors, but
  since it doesn't, this is the workaround.
  [limi]

- Add a migration utility function to load (parts of) GenericSetup
  profiles during migration. This allows us to write configuration changes
  in the form of GenericSetup extension profiles instead of python code.
  Use this to load a new 3.0b1-3.0b2 migration profile.
  [wichert]

- 'News' and 'Events' are no longer "Smart Folders" (or "Collections") in
  new created portals. Instead, they are now "Large Folders" with a
  "Collection" default page named 'aggregator'.
  This closes http://dev.plone.org/plone/ticket/6218.
  [davconvent, nouri, optilude]

- Remove the default_charset property on the portal object during
  migration if it is set to an empty string. This makes sure we do not try
  to use an invalid (ie empty) encoding when exporting GenericSetup
  profiles.
  [wichert]

- Register the tool interface for the membership and workflow tools
  using the CMFCore interface, overriding the CMFDefault registration.
  [wichert]

- Enabled search-current-folder-only option for the quicksearch box.
  [optilude]

- Make the navigation root affect searches (including live searches).
  By default, you will not get search results from outside the navigation
  root.
  [optilude]

- Merged patch from olivluca to properly support the uniqueItemIndex
  iterator.
  [optilude]

- Set the current instance version on site creation so we can migrate
  properly.
  [wichert]

- Added new arguments to the action tools API which allow querying for a
  specific action category or exclude certain action categories or action
  providers from the results in an efficient way.
  [hannosch]

  We exclude all actions from the workflow tool and those in the
  folder_buttons and object_buttons categories by default from the
  dictionary available from the ploneview.
  [hannosch]

- Removed lots of unused actions and the entire object_tabs and global
  action categories. This closes http://dev.plone.org/plone/ticket/6336.
  [hannosch]

- Cleaned up code in unicodehacks.py so we don't have a performance
  penalty for mixed unicode/non-unicode pages.
  [hannosch]

- Micro optimization: Use a truly local variable for language lookup,
  which is faster than getting the value from the globals.
  [hannosch]

- Stop calculating the body text of a document twice in document_view.
  [hannosch]

- Changed order of action providers to fit the way we want to see
  content tabs.
  [davconvent, nouri]

3.0-beta1 - released March 26, 2007
-----------------------------------

- Use plone.session for authentication.
  [wichert]

- Replaced getToolByName calls with getUtility/queryUtility for placeful
  workflow tool.
  [encolpe]

- Changed all mail related templates and methods to use the email_charset
  property. This closes http://dev.plone.org/plone/ticket/5585.
  [hannosch]

- Added email_charset property, which should be used as the charset to
  send mail, so you are not restricted to the default_charset which has to
  be utf-8 right now. This refs http://dev.plone.org/plone/ticket/5585.
  [hannosch]

- Opera 9 is now a supported browser for the rich text editor.
  [duncan]

- Removed computeRoleMap.py, as it can't be deprecated in a safe manner.
  If your product depended on this, you need to update it.
  [limi]

- id="relatedItems" is now a class="relatedItems".
  This closes http://dev.plone.org/plone/ticket/6229.
  [limi]

- Removed references to specific workflow states from the publishing
  process explanation in content_status_history.cpt. This closes
  http://dev.plone.org/plone/ticket/4648.
  [hannosch]

- Increased the calendar_starting_year property to 2001, so the available
  calendar range doesn't end in 2010, which is quite soon ;)
  [hannosch]

- Made the content menu (in plone.app.contentmenu) only show up on the
  main view of an object; on other tabs, it makes less sense, especially
  on the edit tab where it may cause confusion and lead users to
  accidentally cancel their edit operation by clicking a content menu
  link.
  [optilude]

- Removed all mail templates which are part of PasswordResetTool and
  weren't used anymore.
  [hannosch]

- Replaced a few last occurrences of the term member with user. This
  closes http://dev.plone.org/plone/ticket/5792.
  [hannosch]

- Added temporary monkey-patch for GenericSetup's components handler. We
  need to ensure we store Acquisition free tools as utilities.
  [hannosch]

- Properly install PloneLanguageTool during site setup and migrations.
  [hannosch]

- Updated setup code. Archetypes and all its dependencies are installed
  based on GenericSetup extension profiles now.
  [hannosch]

- Add migration code to remove the PlonePAS PloneTool from the site and
  replace it with a standard PloneTool.
  [wichert]

- Improve the test for GRUF presence; it also considered a PlonePAS
  monkeyed PAS as GRUF.
  [wichert]

- Remove GRUF usage for local role handling in PloneTool
  [wichert]

- Updated language dependent portal creation step. We set the default
  language of the portal, the allowed languages and if necessary the
  combined languages support option. If we get a territory code in the
  locale we also set the visible_ids setting to true for non-latin-scripts,
  for which we don't have a IURLNormalizer registered. This closes
  http://dev.plone.org/plone/ticket/5971.
  [hannosch]

- Removed tests/runalltests.py and tests/framework.py as they have
  outlived their usefulness. To run tests use Zope's testrunner:
  ./bin/zopectl test --nowarn -s Products.CMFPlone
  [stefan]

- Added missing migration step addPortletManagers, to add the new portlet
  manager adapters.
  [hannosch]

- Fixed various bugs in the migration code. We need to register additional
  GenericSetup import steps manually or the componentregistry step is not
  available, which new products like CMFEditions depend on. When add-ons
  use this step we need to make sure they are allowed to run all the
  dependent steps, so we needed to make the plone-site step available for
  all extension profiles, by not requiring a flag file anymore. We also
  need to call the enableZope3Site and registerToolsAsUtilities migration
  steps as the first step in every possible version migration, as the
  migration code itself depends on these to be present. Otherwise
  migrating from older versions would fail with ComponentLookupErrors.
  [hannosch]

- Location is now a standard metadata field available for categorizing
  content. This means that you can geotag images, display content with
  location data on a map, etc.
  [limi, nouri]

- Extended the timeout on password resets from 1 day to 1 week by default.
  [limi]

- Fix bug #6227 : Batch-workflowing objects would erroneously give them
  the effective date of the portal object or their container.
  [elvix]

- Registered all standard CMF and Plone tools as local utilities and
  replaced most getToolByName calls with getUtility/queryUtility.
  [hannosch]

- Registered the portal itself as a utility providing IPloneSiteRoot and
  as one providing CMF's ISiteRoot.
  [hannosch]

- Replaced our local component registry with one from
  five.localsitemanager. There is no migration path for existing Plone 3.0
  alpha sites, so make sure to throw them away and recreate new ones.
  Migration from Plone < 3.0 is of course supported.
  [hannosch]

- Optimized the calendar_macros template. Trying to translate integers
  like years or hours wasn't very helpful.
  [hannosch]

- Optimized code in the translation service tool for the calendar_macros
  use case, so we can get rid of the explicit call of the deprecated
  utranslate script.
  [hannosch]

- Added new user/group settings control panel.
  [hannosch]

- Moved version overview and server debug mode to the maintenance control
  panel. Added warning message about missing mail host or email from
  address to the main control panel view.
  [hannosch]

- Added external_links_open_new_window to site properties which controls
  the behavior of mark_special_links.js.
  [hannosch]

- Only show the user friendly types on the navigation control panel.
  [hannosch]

- Excluded x-web-intelligenttext from the list of activated mimetypes.
  [hannosch]

- Remove the folder user action, and re-point the author profile user
  action to point to the users dashboard instead.
  [wichert]

- Add an object_provides index to the catalog. This indexes all
  interfaces provided by an object with their dotted names.
  [wichert]

- Made it possible to look up the ExtensibleIndexableObjectWrapper using
  a multi-adapter on (context, portal). The wrapper now has an additional
  method update() which can update with workflow variables and the like.
  This allows a particular wrapper to be registered for a particular type
  of object, allowing more careful control over the indexing process.
  [optilude]

- Removed ids from portlet templates and turned into classes. This makes
  sure we do not get duplicate ids in our html when multiple instances of
  the same portlet type are created, while still allowing different
  styling of different portlet types
  [wichert]

- Undeprecated the toLocalizedTime script. We are probably going to change
  the approach to be based on Zope3 locales in the next release, so it
  doesn't make sense to force everybody to change their products now.
  [hannosch]

- Renamed Keywords to Categories, and included tags/labels/keywords
  explanation in the help text. User research showed that people
  understand this term better than the other alternatives.
  [limi]

- Make it easy to include javascript for trackers like Google Analytics
  via a new control panel-manageable webstats.js file.
  [mrtopf]

- Added an RSS portlet.
  [mrtopf]

- Removed the unsupported Plone Tableless skin.
  [wichert]

- Added class to the navtree: "navTreeItemInPath", which exists on all
  nodes that are in the current path.
  [limi]

- Added Google/MSN/Yahoo site map support as described on
  http://www.sitemaps.org
  It is disabled by default and can be retrieved via
  http://<portalroot>/sitemap.xml.gz
  [mrtopf]

- Add migration code for the enable_sitemap site property
  [wichert]

- Removed the Undo action (since we have versioning now) - it's too
  complex to be useful for normal users, and admin users have the ZMI.
  Also renamed "Join" action to "Register" and removed the dedicated
  link to the personal Preferences pending addition of the Dashboard link.
  We do not migrate existing sites to these values on purpose - if you
  want these changes, it's easy to fix them in portal_actions on your
  site.
  [limi]

- Set text-transform property to none, it's not 2001 anymore, and the mix
  of uppercase and lowercase was hurting me. Also fixed font size for the
  unreadably small text in Firefox on certain platforms.
  [limi]

- Install kupu via its GenericSetup profile.
  [wichert]

- Renamed the statusmessage of type stop to error and the CSS class from
  portalStopMessage to portalErrorMessage accordingly.
  [hannosch]

- Removed the forms.txt and rendering.txt functional test - there are
  covered by  AddMoveAndDeleteDocument.txt, which is more sane. Also
  update the latter to reflect a label change from plone.app.contentmenu.
  [optilude]

- Deprecated viewThreadsAtBottom and getReplyReplies in favour of a
  viewlet for IBelowContent, defined in plone.app.form.
  [optilude]

- Added all currently used translation domains as PTSTranslationDomains.
  This makes them available as Zope3 translation domain as well, so they
  can be used in pure Zope3 page templates for example.
  [hannosch, philiKON]

- Changed plone_control_panel overview to use a three column layout.
  [hannosch]

- Added migration steps for new security and html filter control panels.
  [hannosch]

- Sanitized control panel names. Removed the redundant settings in titles.
  [hannosch]

- Converted site and skins control panels to be formlib based. Moved the
  Google sitemap option to the site control panel. Fixed migration code
  for maintenance control panel. This closes
  http://dev.plone.org/plone/ticket/6193.
  [hannosch]

- Hide the PAS folder and its plugins from the breadcrumbs.
  [wichert]

- Fixed cropping of utf8 encoded text. cropText script
  is marked as deprecated now.
  This fixes http://dev.plone.org/plone/ticket/6190.
  [naro]

- Remove the default language setting from the site control panel. This
  setting doesn't work anyways right now.
  [hannosch]

- Split the dashboard into four columns. If you have run an earlier
  version of the alpha, you need to re-run the portlets.xml importhandler
  or re-create your portal to be able to use the dashboard.
  [optilude]

- Change the default time and date format. This closes
  http://dev.plone.org/plone/ticket/6172.
  [hannosch]

- On site setup the mail host and email address are left empty.
  This references http://dev.plone.org/plone/ticket/5881.
  [hannosch]

- Renamed "Smart Folder" to "Collection" since it better describes the new
  functionality, made other things more consistent: "Comments" everywhere
  instead of "Discussion", "Publishing Date" instead of "Effective Date",
  better help text on these.
  [limi]

- Ignore a bunch of more required products in the install/uninstall
  control panel form.
  [hannosch]

- Removed last occurrences of portal_status_messages and removed the
  inclusion code in global_statusmessage. This closes
  http://dev.plone.org/plone/ticket/6131.
  [hannosch]

- Removed the old CMF types from the GenericSetup profiles. This closes
  http://dev.plone.org/plone/ticket/6156.
  [hannosch]

- Removed the news_listing template that hasn't been in use since Plone
  2.0 (it wasn't working anyway). It was replaced by the summary view in
  Plone 2.1, and deprecated then, which means it should be safe to remove.
  [limi]

- Fixed encoding problem when sending out registration emails
  [jvloothuis, ender]

- Deprecated relaxed mode of the normalizeString methods in favour of
  direct usage of the normalizers in plone.i18n.
  [hannosch]

- Merged plip174-reusable-i18n branch. Normalization logic and language
  handling are based on plone.i18n / plone.app.i18n now.
  [hannosch]

3.0-alpha2 - released February 13, 2007
---------------------------------------

- Deprecated the isRightToLeft method on the ploneview in favour of the
  is_rtl method on the plone_portal_state view.
  [hannosch]

- Added Google-specific extensions to the robots.txt file to deny it from
  indexing a gazillion sento_forms. The standard doesn't allow for
  wildcards boot Google does.
  [elvix]

- Added robots.txt file. This should remove some unwanted not-found-errors
  and give fresh Plone-admins something to customise for robots if they
  want it.
  more info about robots.txt here:
  http://www.robotstxt.org/wc/norobots.html
  [elvix]

- Commented out the IE-specific styling of textarea scrollbars from
  IEFixes.css. Plone uses standard scrollbars from 3.0 onwards, but if you
  want them back, they can easily be uncommented.
  [limi]

- Added some classes to document_byline.pt for more flexibility when
  styling this template. This closes
  http://dev.plone.org/plone/ticket/5025
  [spliter]

- Deprecated skin related methods of the Plone tool. The functionality is
  provided by the skins tool itself for some time now.
  [hannosch]

- Updated the various mixed Unicode/UTF-8 support patches to be compatible
  with Zope 2.10.2, which is required now as a minimum Zope version.
  [hannosch]

- Did some minor import locations cleanup. Deprecated i18n related methods
  in utils.py and importing IndexIterator from ploneview.py.
  [hannosch]

- Added simply optimization to the getReplyReplies script, avoiding some
  calculations when there are no replies and removed the custom
  getDiscussionFor method from CMFPlone's DiscussionTool, as it wasn't
  needed anymore.
  [hannosch]

- Fixed an unsafe usage of hasattr in computeRelatedItems with
  base_hasattr.
  [hannosch]

- Removed obsolete factory type information for the Plone folder classes.
  [hannosch]

- Deprecated the getOrderedUserActions script. It was only used in the
  global_personalbar to enforce a certain logical order of the actions,
  but action categories support ordering themselves now, so the script was
  obsolete.
  [hannosch]

- Deleted folder_localrole_form and its scripts, since this is now
  provided in the @@sharing view. That felt good. Added an alias with
  a deprecation warning in plone.app.layout so that old links still work.
  The alias will be gone in 4.0.
  [optilude]

- Moved accessibility elements from base.css to invisibles.css, since they
  should remain even if you do a total customization.
  [limi]

- Removed Five from the core versions overview in the plone control panel.
  Five will probably evolve as a set of independent packages rather than
  one monolithic package so its version isn't of any particular interest
  anymore.
  [hannosch]

- Added Reader and Editor local roles, and merged in support for the new
  sharing page, at the @@sharing view.
  [optilude]

- Add support for OpenID authentication.
  [wichert]

- Make it possible to use the plone.session PAS plugin. This provides
  a scalable method to use session authentication in Plone sites.
  [wichert]

- Converted PlonePAS installation to be GenericSetup based and moved all
  user/group related setup functions there as well. Also removed explicit
  GroupUserFolder installation as it isn't needed anymore.
  [hannosch]

- Added new SiteManagerCreatedEvent that is called right after the portal
  is enabled as a site. We can use this to call the setHooks and setSite
  functions which are mandatory during test runs, before any other
  GenericSetup import step tries to call any local component.
  [hannosch]

- Decoupled some more of the GenericSetup import steps. The plone-site
  step only creates the local component registry and enables the portal
  object as a site manager. This is needed as steps using local components
  depend on this step while not much else in the site may have been
  configured yet.
  The plone-content step adjusts the initial content and is run last as it
  depends on everything else in the portal having been already set up.
  [hannosch]

- Added an alias view 'login' (aka '@@login') to let people use /login
  to get to login_form (it perform a redirect). This is also now a
  reserved id.
  [optilude]

- Merged plone.app.contentrules, your friendly content rules engine
  [wayworn, optilude]

- Moved deprecated zcml declarations to its own file deprecated.zcml in
  order to make it easy to spot those or turn them off.
  [hannosch]

- Add a new interface INonInstallable for which you can register named
  utilities that provide a list of profiles that should not be available as
  installable during site creation. We exclude certain products that are
  installed anyways by Plone from the config screen this way.
  [hannosch]

- Use the INonInstallable interface in CMFQuickInstallerTool to exclude
  some products from the list of installable products in the ZMI and
  install/uninstall control panel screen. Otherwise CMFDefault, CMFUid,
  etc. would show up in the list.
  [hannosch]

- Added support for plone.app.redirector to the 404 template. This enables
  automatic redirects when an object has been moved or renamed, and offers
  suggested search results on the 404 page otherwise.
  [optilude]

- Merged changes necessary to support PLIP125 Link Integrity, mostly found
  in the plone.app.linkintegrity package.
  [witsch, optilude]

- Removed the setup tab from the migration tool. It wasn't working anymore
  and the functionality can be found on the controlpanel tool anyways.
  [hannosch]

- Fixed a bug in the require_login script calling a non-existent method on
  the migration tool.
  [hannosch]

- The controlpanel and migration tools are registered as local utilities
  now as well.
  [hannosch]

- Merged in kss.
  [ree]

- Finished multilingual front-page support code. The front page which is
  created at portal creation time is now localized to the browser language
  used while creating the portal, as long as there is a complete
  translation of the page.
  [hannosch]

- Merged generalised next/previous navigation into plone.app.layout
  (interfaces, viewlet), CMFPlone (rel links in header.pt, tests) and
  ATContentTypes (adapter for IATFolder).
  [henri, pelle\_, trollfot, optilude]

- The interface and translation service tools are registered as local
  utilities now.
  [hannosch]

- Exposed the member preference panels in the prefs portlet. This closes
  http://dev.plone.org/plone/ticket/3083.
  [hannosch]

- Added javascript and css to switch between schemas in edit page.
  [fschulze]

- Removed properties tab for all ATCT types.
  [fschulze]

- Moved Products.CMFPlone.browser.contentmenu to plone.app.contentmenu.
  Note that the tests remain in CMFPlone for now (so that they get run
  more often, and to avoid having to replicate dummies etc in the new
  location).
  [optilude]

- Moved date/time formatting related messages to it's own domain called
  plonelocales. Message files in this domain are translated directly by
  the Zope 3 translations service, which results in a major speed increase
  for date/time formatting.
  [hannosch]

- Moved new controlpanels to its own package (plone.app.controlpanel).
  [hannosch]

- Moved various interfaces and utilities - IDefaultPage, INvigationRoot,
  INavtreeStrategy, INavigationQueryBuilder and the buildFolderTree()
  and getNavigationRoot() helper functions - to plone.app.layout. This
  reduces the dumping-ground feeling of CMFPlone.browser, leaving it
  free to focus on actual views that implement CMFPlone look-and-feel and
  policy, and provide a saner dependency/import location for third party
  components needing these tools.
  [optilude]

- Gave IContentIcon a html_tag() helper method to make rendering the
  icon one line (<img tal:replace="structure item_icon/html_tag" />)
  rather than ten or so. Also made the properties properties rather than
  functions.
  [optilude]

- Removed outdated version of listFilteredActionsFor from the actions
  tool.
  [hannosch]

- Deprecated cache_decorator in browser/ploneview.py (formerly plone.py),
  in favour of plone.memoize's instance.memoize decorator. Replaced all
  uses of cache_decorator in CMFPlone with plone.memoize.
  [optilude]

- Renamed Products.CMFPlone.browser.plone (plone.py) to
  Products.CMFPlone.browser.ploneview (ploneview.py). The naming
  was causing conflicts with the 'plone' namespace package. A
  module alias remains during the deprecation period (i.e.
  it will be removed in Plone 4.0).
  [optilude]

- Use img tags instead of css classes for icons (PLIP 178).
  [fschulze]

- Added missing ATRelativePathCriterion to the default profile.
  [stefan]

- Some minor code modernizations in the FactoryTool.
  [hannosch]

- Added formlib based mail and search control panels.
  [hannosch]

- Removed the view alias of index.html for all standard content types.
  This makes it possible to create and upload files called index.html to
  the site, which is quite common when batch importing old sites into the
  site.
  As someone might rely on the former behaviour, we do not migrate
  any existing type information. This closes
  http://dev.plone.org/plone/ticket/4837.
  [hannosch]

3.0-alpha1 - released November 24, 2006
---------------------------------------

- Update installation instructions for the new Plone release.
  [wichert]

- Added calendar control panel based on formlib. This is related to
  http://dev.plone.org/plone/ticket/5271.
  [hannosch]

- Moved global_contentmenu to plone_deprecated
  [optilude]

- Injected Plone 2.1.4 into the migration chain.
  [stefan]

- Removed bogus scripts from workflow actions, and introduced some BBB
  code to ensure that if people are using those scripts and they don't
  exist, the old fallback (content_status_modify) is still used.
  [optilude]

- Plone 4.0 will introduce the role "Power User" to make it possible to
  hide advanced functionality from casual users. It you have any
  deployments that use this role name, now would be a good time to rename
  that role and stop using it in product code.

- Update migrations for portlets, and kick the meta.zcml in
  plone.app.portlets.
  [optilude]

- First day of week in the calendar is Monday now in Plone by default.
  This closes http://dev.plone.org/plone/ticket/5882.
  [hannosch]

- Added option to choose different base profile while creating a new Plone
  site. This closes http://dev.plone.org/plone/ticket/5890.
  [hannosch]

- Deal with CMFDefault renaming _checkEmail to checkEmailAddress.
  [wichert]

- Removed unused scripts from the extensions folder.
  [hannosch]

- Added some notes about CMFEditions and CMFDiffTool installation.
  [hannosch]

- Added first part of multilingual front-page support code.
  [hannosch]

- livesearch_reply.py wrote quotes (") in the title-attribute. malformed
  XML was generated. replaced quotes by &quot;.
  [jensens]

- Merged plip142-componentised-content-menu
  http://plone.org/products/plone/roadmap/142.
  [optilude, hannosch]

- Merged plip148-cmf21 bundle. This implements
  http://plone.org/products/plone/roadmap/148 and
  http://plone.org/products/plone/roadmap/161.
  [hannosch]

- Merged PLIP 8 versioning bundle
  http://plone.org/products/plone/roadmap/8.
  [wichert]

- Converted some tests to inline doctests and some others to real unit
  tests as opposed to integration tests.
  [hannosch]

- Changed the logo template 'global_logo' to not use the image replacement
  approach, but use a straightforward link/image approach instead.
  Sometimes Plone tries to be too smart for its own good. ;)
  This also fixes the horizontal scrollbar problem in IE6 for RTL layouts.
  [limi]

- Silenced the utf-8 / Unicode DeprecationWarning. We should only emit
  warnings once we fixed this in all standard cases ourselves.
  [hannosch]

- Added migration for the css files added by limi in the previous entry.
  [jladage]

- Split up the CSS into a couple of new modules to ease customization.
  [limi]

- Added an optional keyword argument to the date_components_support script
  that allows to specify the minute steps. It still defaults to five.
  This closes http://dev.plone.org/plone/ticket/5178.
  [hannosch]

- Deprecated some more unused skins scripts: extract_date_components,
  getPersonalFolderFor, navigationCurrent, navigationLocalRelated and
  rejectAnonymous.
  [hannosch]

- Deprecated the never used nor functional prefs_workflow* control panels,
  we are better of with a fresh start on these anyways.
  [hannosch]

- Do not set initial descriptions for the member folders, as these often
  ended up in a translation the user did not want or understand. We only
  use the simply username as a title now, which is language independent.
  This fixes http://dev.plone.org/plone/ticket/4214.
  [hannosch]

- Updated the text on the member search form to be more user friendly.
  This closes http://dev.plone.org/plone/ticket/4675.
  [hannosch]

- Deprecated our unmaintainable 'how-to enable cookie' instructions.
  This closes http://dev.plone.org/plone/ticket/4602.
  [hannosch]

- Added error tolerant version of FasterStringIO to unicodeFallbackPatch.
  This is monkey patched into the Zope3 tal and pagetemplate modules and
  replaces the monkey patch found in PlacelessTranslationService so far.
  [ree, hannosch]

- Deprecated PloneContent. Use (marker) interfaces instead to get a way to
  check for a functionality that is common to some types.
  [hannosch]

- Deprecated the CMFPlone implementation of LargePloneFolder. Use
  ATBTreeFolder from ATContentTypes instead.
  [hannosch]

- Added unicodeFallbackPatch that allows to use utf-8 encoded strings to
  be used inside the Zope3 TAL engine.
  [ree, hannosch]

- Fixed the 'Unauthorized: You are not allowed to access 'Creator' in this
  context' error that was raised in the testCookieAuth tests.
  [hannosch]

- Using new 'visualIcon' css class to allow much smaller generated.css
  and RTL.css. When new content types are installed, then generated.css
  will grow much less then before and RTL.css will not grow at all
  anymore. The footprint of action icons is also smaller now.
  [fschulze]

- The portal object is set up as a Zope3 site with a local site manager.
  [hannosch]

- Removed CMFPlone.MemberData. This class is never used, and the future
  is with PAS-based objects instead of membership/memberdata tools.
  [wichert]

- Fixed deprecation warnings for the ZCML content directive.
  [hannosch]

- Removed deprecated createTopLevelTabs from PloneTool and utils. Use the
  topLevelTabs method of the INavigationTabs view instead.
  [hannosch]

- Removed deprecated CustomizationPolicy and old site creation machinery.
  [hannosch]

- Removed deprecated CSS styles from deprecated.css.
  [hannosch]

- Removed deprecated scripts from the plone_deprecated skins layer.
  [hannosch]

- Removed lots of deprecated values from the PloneView.
  [hannosch]

- Removed deprecated FolderWorkflow, PloneWorkflow and PloneUtilities
  classes. Removed aliases for base_hasattr and transaction_note from
  CMFPlone. Import these from CMFPlone.utils. Removed security
  declarations for zLOG levels. zLOG usage was replaced by Python's
  logging module.
  [hannosch]

- Removed five:traversable from configure.zcml as it is not needed anymore
  for Zope 2.10.
  [hannosch]

- Removed bbb code for MessageIDFactory, queryMultiAdapter, transaction
  and CatalogTool._initIndexes.
  [hannosch]

2.5.4 - Unreleased
------------------

- No longer call invokeFactory twice when creating objects in
  portal_factory. Fixes http://dev.plone.org/plone/ticket/6595
  Nice catch nouri :-)
  [alecm]

2.5.3 - Final - released May 16, 2007
-------------------------------------

- Further optimized the migrations from older Plone versions. We reindex
  the whole catalog once and only once, independent of the Plone version
  we start migrating from.
  [hannosch]

- Made migration twice as fast, it was recataloging unnecessarily.
  [hazmat][limi]

_ Add a new IHideFromBreadcrumbs interface. Items marked with this
  interface will not be shown in the breadcrumb trail. Mark the portal
  factory with this interface so it no longer pollutes the breadcrumbs.
  [wichert]

- Made CatalogTool.ExtensibleIndexableObjectWrapper a subclass of the
  CMFCore.CatalogTool.IndexableObjectWrapper class to ensure Plone
  doesn't miss on improvements made there. EIOW instances now proxy
  Zope3 interface declarations of the wrapped object.

2.5.2 - Orb - released January 16, 2007
---------------------------------------

- Fix issue with drag and drop caused by changing of css ids in
  folder_contents.
  [alecm]

- Added some classes to document_byline.pt for more flexibility when styling
  this template. This closes
  http://dev.plone.org/plone/ticket/5025
  [spliter]

2.5.2 - Release Candidate - released January 3, 2007
----------------------------------------------------

- In livesearch results, don't append ... at the end, when the length of
  the title or description is exactly the limit. This closes
  http://dev.plone.org/plone/ticket/5989.
  [hannosch]

- Do not display the right column on prefs_main_template anymore, as it
  was unneeded and could cause design problems. This closes
  http://dev.plone.org/plone/ticket/5803.
  [hannosch]

- Moved the global_cache_settings call in main_template before the call to
  header.pt as otherwise the encoding in the header would not be defined
  and fall back to ZPublishers default_encoding. This closes
  http://dev.plone.org/plone/ticket/6013
  [hannosch]

- Optimized the check_id.py uniqueness check to not use contentIds,
  fixes http://dev.plone.org/plone/ticket/5976
  [alecm]

- Add search term highlighting to livesearch result links.
  [alecm]

- links in Contents table behave as they should now - show the "pointer"
  hand when hovering the mouse over them. It was broken due to ajax
  sorting feature somehow
  [spliter]

- event_view.pt has a better position for details table now, letting
  byLine and Description info to be content-wide and not to be shifted to
  the left, bacuse of Details table
  [spliter]

- main table for columns (#portal-columns) should not have paddings or
  spacings - they can confuse when styling. Fixed with CSS for the table
  cells, thanks to deo ;)
  [spliter]

- Make the parameters for member image scaling more easily configurable
  by putting them in a mutable data structure.  Eventually, we should
  provide a TTW configuration for this.
  [alecm]

- Make hasIndexHtml script more efficient for BTreeFolders.  Fixes
  http://dev.plone.org/plone/ticket/5769
  [alecm]

- Add event support to OrderedContainer so that moveObjectToPosition
  doesn't break on Zope 2.9.  Should fix
  http://dev.plone.org/plone/ticket/5961
  [alecm]

- Make css ids for rows in folder_contents sane.  Fixes
  http://dev.plone.org/plone/ticket/5940
  [alecm]

- Make various icons in folder_contents explicitly render alt tags,
  because the rendering of those images magically picks up items named
  'alt' in the context, which breaks the page.
  Fixes  http://dev.plone.org/plone/ticket/5934
  [alecm]

- Don't assume portal_catalog when reindexing during ownership change.
  Fixes http://dev.plone.org/plone/ticket/5063
  [alecm]

- Ensure rss_template max items is an integer.  Should fix
  http://dev.plone.org/plone/ticket/5553
  [alecm]

- Applied patch from aaronv to add includeTop setting to navigation
  prefs form.  Fixes http://dev.plone.org/plone/ticket/5519
  [alecm]

- Made standard_error_message more tolerant of security issues and
  acquisition problems.  Fixes http://dev.plone.org/plone/ticket/5955
  [alecm]

- Fixed issue with search for members of groups, using patch from
  derek_richardson.  Fixes http://dev.plone.org/plone/ticket/5902
  [alecm]

- Use some url unquoting to ensure that the rename form redirects to the
  correct url after rename, even if quoted characters are involved.  Fixes
  http://dev.plone.org/plone/ticket/5843
  [alecm]

- Use current_page_url instead of ACTUAL_URL for accessibility anchors.
  Fixes http://dev.plone.org/plone/ticket/5777
  [alecm]

- Made the error displayed on SMTPRecipientsRefused during password reset
  not display the email address, as this is an undesirable privacy
  leakage. Fixes http://dev.plone.org/plone/ticket/5962
  [alecm]

- Applied the Hotfix for CVE-2006-4249, which also fixes
  http://dev.plone.org/plone/ticket/5906
  [wiggy, alecm]

- Non-ascii characters in actions used in the portal tabs provoked an
  UnicodeDecodeError. This closes http://dev.plone.org/plone/ticket/5791.
  [hannosch]

- Fixed another UnicodeDecodeError in livesearch_reply.
  This fixed http://dev.plone.org/plone/ticket/5828.
  [hannosch]

- Added a general safe_unicode method to utils.py, which can be used to
  convert any Unicode, 'utf-8' or 'ascii' encoded string to Unicode.
  [hannosch]

- Added button tag styling that conforms to the standard input button
  look.
  [limi]

- Added optgroup styling, since the default in Firefox looks like crap.
  [limi]

- Fixed the Live search error: 0x80040111 (NS_ERROR_NOT_AVAILABLE). This
  closes http://dev.plone.org/plone/ticket/4519.
  [deo]

- Injected Plone 2.1.4 into the migration chain.
  [stefan]

- Lots of minor whitespace corrections, found by using the new i18ndude
  3.0 which is based on zope.tal.talgettext for extraction of translation
  files.
  [hannosch]

- Fixed a minor spelling inconsistency in folder_localrole_form.
  [hannosch]

- Fixed flawed lookup of email_from_address in send_feedback scripts. This
  closes http://dev.plone.org/plone/ticket/5839.
  [hannosch]

- Added option to choose different base profile while creating a new Plone
  site. This closes http://dev.plone.org/plone/ticket/5890.
  [hannosch]

- Removed redundant getToolByName call in send_feedback_site. This closes
  http://dev.plone.org/plone/ticket/5863.
  [hannosch]

- Fixed the calendar portlet to display correctly in Internet Explorer 7.
  [limi]

- Updated links in the automatically generated front-page.
  [hannosch]

- Added a few macro hooks in personalize_form and prefs_user_details to
  allow at least some form of easy customization without the need to
  customize the entire forms. Now it looks for a file
  'additional_memberdata' in your skin and uses the macros in there to
  inject them into these forms.
  [ender]

- livesearch_reply.py mixed up utf-8-encoded strings and unicode strings
  leading to unpredictable UnicodeDecodeErrors. This fixes
  http://dev.plone.org/plone/ticket/5828.
  [ajung]

- livesearch_reply.py wrote quotes (") in the title-attribute. malformed
  XML was generated. replaced quotes by &quot;.
  [jensens]

2.5.1 - released September 28, 2006
-----------------------------------

- The content tab selection logic now checks the request in addition
  to template_id when trying to determine which tab should be
  selected.
  [rocky]

- Noted the new hard dependency on ElementTree that was introduced in the
  Marshall product as of Plone 2.5.1.
  [hannosch]

- The plone_various and plone-final steps now honour
  GenericSetup conventions and only run when a config file is present for
  them. ExtensionProfiles no longer need to override these steps. Fixes
  http://dev.plone.org/plone/ticket/5823
  [mj]

2.5.1-rc1 - released September 11, 2006
---------------------------------------

- Fixed an UnicodeDecodeError in enableSyndication script. This closes
  http://dev.plone.org/plone/ticket/5750.
  [hannosch]

- Adjusted button CSS to have overflow: visible because Internet Explorer
  makes them very wide in foreign languages like Finnish. This fixes
  http://dev.plone.org/plone/ticket/5461 - thanks to Mikko.
  [limi]

- Made login_form and default_error_message not invoke the portlets, since
  they are irrelevant and expensive in those forms. Also made the error
  template a valid HTML document.
  [limi]

- Added description in the dict in WorkflowTool's getTransitionsFor.
  [ender]

- Corrected the log_exc method in log.py to actually log the exception, as
  it was done before replacing zLOG with Python's logging module.
  [hannosch]

- Make the object_delete and folder_delete methods require non-GET
  requests. This is a bit of a band-aid and it is likely we will want
  to do the same for other object actions which could be easily triggered
  by a crawler (a paste for instance, which may have been preceded by a
  cut or copy). Related to http://dev.plone.org/plone/ticket/4886
  [alecm] [limi]

- Make the syntool methods for enabling and disabling syndication check
  for the Manager properties permission on the object.
  [alecm]

- Making text/* not render inline for security reasons (Internet Explorer
  renders these blindly, no matter that they are not text/html), and
  fixing inline rendering of Office documents and PDFs in the process.
  [limi]

- Fix member portrait handling by automatically scaling all incoming
  images using PIL. This will throw an IOError on any invalid image and
  also save some bandwidth and space in the zodb.
  [alecm]

- Added method and management template to membership tool to cleanup
  members with bad images.
  [alecm]

- Made 'setuphandlers.PloneGenerator.setupPortalContent' more
  robust by checking if the Members folder is really there.
  [nouri]

- Copied '_getSecurity' from Archetypes.utils to avoid a dependency.
  Plone should not import from Archetypes to minimize coupling.
  [stefan]

- Added a Unicode and UTF-8 aware case normalizer to the plone_lexicon
  pipeline. Goes with the fix for http://dev.plone.org/plone/ticket/5231
  [stefan]

- Circumvented a UnicodeDecodeError on smart folders editing view. This
  closes http://dev.plone.org/plone/ticket/5746.
  [hannosch]

- Added new css class visualIcon. This will be used to make generated.css
  much smaller in Plone 3.0 and is introduced now, so people can see how
  this will affect templates. Only templates which use css to add icons
  for content types are affected.
  [fschulze]

- DiscussionTool.cookReply needs to be available to anyone who can comment
  on an item, otherwise the comment will not be cooked and we get HTML
  injection.  This fixes http://dev.plone.org/plone/ticket/5718
  [alecm]

- Made the code in utranslate more error resilient and added tests for it.
  [rafrombrc] [hannosch]

- Enhanced accessibility of adjacent links in main_template. This fixes
  http://dev.plone.org/plone/ticket/5210.
  [hannosch]

- Removed some unnecessary hyphens from date_components_support. This
  fixes http://dev.plone.org/plone/ticket/5711.
  [hannosch]

- Added Five and CMF version to the control panel version overview. This
  closes http://dev.plone.org/plone/ticket/5345.
  [hannosch]

- Made getInheritedLocalRoles in PloneTool more error resilient. This
  closes http://dev.plone.org/plone/ticket/5542.
  [hannosch]

- Added some workaround code for the general misbehaving utranslate and
  uLocalizedTime methods. They should return Unicode now again, but right
  now they only work for the single supported site encoding of utf-8.
  This fixes http://dev.plone.org/plone/ticket/5609.
  [hannosch]

- Synced table-less and table-based main_template again. This fixes
  http://dev.plone.org/plone/ticket/5696.
  [hannosch]

- Fixed incorrect status message after bad login attempt. This closes
  http://dev.plone.org/plone/ticket/5695.
  [hannosch]

- According to GenericSetup.interfaces.IProfileRegistry: when an extension
  profile is registered for 'None', it should be available in any type of
  site. Fixed CMFPlone.factory to include such profiles.
  [stefan]

- Made PloneTool.browserDefault check if the default page it is trying to
  render is the folder itself, and prevent it from doing so (which would
  cause an endless loop). Fixes http://dev.plone.org/plone/ticket/5704.
  [alecm]

- Applied patch from paregorius to add ids to all visualClear divs. Fixes
  http://dev.plone.org/plone/ticket/4145.
  [paregorius] [alecm]

- Applied patch from paregorius to make the LiveSearch div vanish in IE
  as needed. Fixes http://dev.plone.org/plone/ticket/5705.
  [paregorius] [alecm]

- Made PloneTool.browserDefault check for a result of None from getLayout
  and raise a sensible error.  Generally this means that the FTI is
  missing or otherwise incorrect.
  Fixes http://dev.plone.org/plone/ticket/5676.
  [alecm]

- Added migration to reindex the catalog which is necessary for the
  changes made for http://dev.plone.org/plone/ticket/5569 and
  http://dev.plone.org/plone/ticket/5231.
  [alecm]

- Made is_folderish and isStructuralFolder respect the z2
  INonStructuralFolder interface as well as the z3 one. Fixes
  http://dev.plone.org/plone/ticket/5592 and
  http://dev.plone.org/plone/ticket/5569.
  [alecm]

- Changed all of the action conditional expressions checking for
  the existence of 'member' to explicitly use 'member is None'
  or 'member is not None' rather than just using truth or falsehood
  of the member object.
  [rafrombrc]

- Added a workaround for erroneous indexing behavior for words containing
  non-ascii characters. These were treated as word breaks so far. The code
  works for a site encoding of 'utf-8' now as well as proper unicode
  usage. This closes http://dev.plone.org/plone/ticket/5231.
  [hannosch]

- Added migration to remove plone.css from portal_css. Fixes
  http://dev.plone.org/plone/ticket/5614.
  [alecm]

- Fixed wrong usage of label tag. Added one for attribute that was
  missing. This closes http://dev.plone.org/plone/ticket/5539.
  [ender]

- Added test that ensures the language is getting set in header.
  This is related to http://dev.plone.org/plone/ticket/5444 and
  http://dev.plone.org/plone/ticket/4770.
  [hannosch]

- Fixed folder_summary_view ignored allowAnonymousViewAbout.
  http://dev.plone.org/plone/ticket/5678
  [ender]

- Fixed language setting in the html page header. This closes
  http://dev.plone.org/plone/ticket/5444.
  [hannosch]

- Added a few tests for the calendar view.
  [hannosch]

- Fixed the problem where you cannot select items in folder_contents in
  Safari. All non-draggable elements must have the 'notDraggable' CSS
  class now. This closes http://dev.plone.org/plone/ticket/5586.
  [deo]

- Fixed handling of login_time and last_login member properties:
  last_login_time is now the time of the previous login and login_time is
  the time of the current login. This fixes
  http://dev.plone.org/plone/ticket/5471.
  [wichert]

- Ignored the ' character when normalizing strings. This implements part
  of http://dev.plone.org/plone/ticket/5664.
  [wichert]

- Improved test for autogenerated ids to handle content types with an
  underscore in their id. This fixes
  http://dev.plone.org/plone/ticket/5560.
  [wichert]

- Using 'indexObject' instead of 'reindexObject' for
  CatalogTool.clearFindAndRebuild works just as well, but does not
  touch every object and cause a monster transaction to be committed.
  [stefan]

- The list of addable types in a folder is now ordered according to the
  translated title and not the English title anymore. This closes
  http://dev.plone.org/plone/ticket/1760.
  [hannosch]

- Add GenericSetup import and export steps for the portal factory.
  [wichert]

- Fixed a username vs userid confusion in the member search page and
  bring the implementation inline with the help text. This fixes
  http://dev.plone.org/plone/ticket/5657.
  [wichert]

- Small spelling corrections in reconfig_form. This closes
  http://dev.plone.org/plone/ticket/5552.
  [hannosch]

- Event time and location aren't considered byline information in
  folder_listing anymore and thus visible if allowAnonymousViewAbout is
  disabled. This closes http://dev.plone.org/plone/ticket/5573.
  [hannosch]

- Corrected RSS search template to show correct numbers. This closes
  http://dev.plone.org/plone/ticket/5211.
  [hannosch]

- Modified login logic to work for sites which do not use the cookie
  plugin or still use GRUF.
  [wichert]

- Added support for the hCalendar/hCard standard for events. This closes
  http://dev.plone.org/plone/ticket/4102. Thanks, Nate.
  [hannosch]

- Changed setupSite.py to import 'Zope2' instead of 'Zope'. Could
  cause confusion on case-insensitive filesystems with 'zope'.
  [sidnei]

- Fixed bug in folder_contents causing all links to get /folder_contents
  appended as well.
  [optilude]

- Changed all action conditions that were simply "member" or
  "not:member" to be "python:member" or "python:not member" to
  prevent member object from being called, leading to infinite
  recursion in certain cases.
  [rafrombrc]

- Fixed 'reindexContentObject' in CatalogTool.py so that it doesn't
  set the modification date to now due to some AT "convenience".
  [nouri]

- Cleaned up the localrole form to support searching for either a users
  full name or login name; both at once does not work.
  [wichert]

2.5 - released June 16, 2006
----------------------------

- Officially deprecated portlet_related which was slated for removal since
  Plone 2.1.
  [hannosch]

- Fixed invalid URL for events/previous link in events portlet. This
  closes http://dev.plone.org/plone/ticket/5582.
  [hannosch]

- Added missing i18n magic to the dummy workflow transition labeled
  'No change' in content_status_history.cpt.
  [hannosch]

- Fix rename from the action menu when using virtual hosting. Thanks to
  Daniel Nouri, Maurits van Rees, Alec Mitchell and Stefan Holek for
  pointers and code.
  [optilude]

- Small fix to avoid an AttributeError in @@plone when viewing objects
  without isPrincipiaFolderish, in general uses of aq_explicit should be
  conditional.
  [alecm]

Release candidate 3 - released June 13, 2006

- Added missing nocall: for toLocalizedTime in mail_password_template.pt.
  Fixes http://dev.plone.org/plone/ticket/5568
  [alecm]

- Added deprecation warnings for the old site creation machinery.
  [hannosch]

- Fixed last deprecated occurrences of portal_object. Use portal instead.
  [hannosch]

Release Candidate 2 - released June 8, 2006

- Fixed issue with encoding of translated ui strings in javascript.
  [ree, nouri]

Release Candidate 1 - released June 3, 2006

- Deleting objects in the portal root now requires the user to have the
  'Delete objects' permission on both the portal and the objects to be
  deleted.  This makes the rules for object deletion consistent between
  the portal and all other folderish objects in the portal (at least those
  based on BasePloneFolder or AT's BaseFolder). This fixes
  http://dev.plone.org/plone/ticket/2925
  [alecm]

- Don't propose local workflow policy configuration iw we aren't in a
  folderish type. We don't allow it on plone root too.
  [encolpe]

- Finish worklists implementation with workflow id and complete guard
  filtering.
  [encolpe]

- Polished HTML in livesearch_reply.py. It generated <LI> element
  without the <UL> when there are no livesearch results.
  [spliter]

- Added missing 'Apply' button in group preferences again.
  This closes http://dev.plone.org/plone/ticket/5544.
  [hannosch]

- Added a few functional tests using 'zope.testbrowser', see
  'AddMoveAndDeleteDocument.txt' and 'LoginAndLogout.txt'.  These
  should eventually replace the 'rendering.txt' and 'forms.txt'
  tests.

  All ``*.txt`` files in the tests/ directory are now picked up by
  ``test_functional.py``'.  I'm open to change here.

  Note that these tests are only run if you have Five >= 1.4
  [nouri]

- Now that five:traversable handles multiple inheritance better, we can
  just make some common base classes traversable. Fixes issues with
  CompositePack.
  [alecm]

- Fix several wrong usages of the 'label' tag.
  [nouri]

- Added little spamProtect.py enhancement, to allow overwriting of the
  name that should be shown. This closes
  http://dev.plone.org/plone/ticket/4868.
  [hannosch]

- Use sort_limit in the search for portlet_recent. Fixes
  http://dev.plone.org/plone/ticket/5520
  [alecm]

- Expose allowAnonymousViewAbout and allowRolesToAddKeywords in the
  site configuration configlet. Fixes
  http://dev.plone.org/plone/ticket/5275
  [wichert]

- Move the 'mail password' text and link on the login form so the tab
  order is more sane. Fixes http://dev.plone.org/plone/ticket/5516
  [wichert]

- Rename 'large site' option to 'Many users/groups', which covers its
  meaning properly. If more similar options are added later we can group
  those in a new 'large site' option.
  fixes http://dev.plone.org/plone/ticket/5451
  [wichert]

- When changing ownership of an object the new owner is identified by a
  userid, not the username. Adjust the implementation accordingly. This
  fixes http://dev.plone.org/plone/ticket/5535
  [wichert]

- Fixed spelling error in livesearch. This closes
  http://dev.plone.org/plone/ticket/5425
  [hannosch]

- Added workarounds so the rounded corners for portlets work in Internet
  Explorer too.
  [limi] [spliter]

- Moved column padding to public.css to make sure it doesn't stick around
  when doing customizations of the site theme. It used to be in
  columns.css.
  [limi]

- Fixed private attribute access in PloneBaseTool createExprContext to use
  the API. This way it will also work with the Zope3 TAL engine.
  [hannosch]

Beta 2 - released May 17, 2006

- Added 'style_slot' to main_template for compatibility with newer CMF
  versions, and Five applications.
  [siebo]

- Updated the GenericSetup profile format to CMF1.6-style. No
  configuration changes were made, only format changes.
  [hannosch]

- Various small i18n markup fixes. Updated folder_edit_form to conform to
  the same style as the Archetypes based edit forms, as it is still used
  for the Plone site object.
  [hannosch]

- Added smart folder sub-topic listing to all available smart folder view
  templates. Fixes http://dev.plone.org/plone/ticket/5349.
  [alecm]

- Added link to error reference on plone.org to error log form.
  Fixes http://dev.plone.org/plone/ticket/5478.
  [brcwhit]

- Fixed showEditableBorder.py to check the following permission
  before checking whether a user is anonymous: Modify portal
  content, Add portal content, Review portal content.
  This closes http://dev.plone.org/plone/ticket/5117.
  [brcwhit]

- Fixed livesearch issues.
  This closes http://dev.plone.org/plone/ticket/5204 .
  [ree]

- Set access for all plone control panel forms to View =
  0:Manager. Closes http://dev.plone.org/plone/ticket/5434.
  [brcwhit]

- Fixed extra space in changeSiteActions function in some migrations.
  This closes http://dev.plone.org/plone/ticket/5161.
  [hannosch]

- Fixed the float bug on Events' view page
  This closes http://dev.plone.org/plone/ticket/5226
  [spliter]

- Fixed bug in login_success. If you did not came_from somewhere, it would
  still offer you to go there. Changed this to portal_url instead.
  This closes http://dev.plone.org/plone/ticket/5496.
  [hannosch]

- Added migrations to get rid of deprecation warnings due to actions which
  still use the old scripts.  Gave @@plone.isRightToLeft a sane default
  value.  Made the quoting conventions used in the XML profiles a bit more
  consistent.
  [alecm]

- Simplified action url/condition expressions by using @@plone view
  methods.  There are now no more URL expressions that use 'python:'
  expressions.
  [alecm]

- Re-add folder_edit_form which is still used to edit the site root.
  This closes http://dev.plone.org/plone/ticket/5430.
  [hannosch]

- Fixed some i18n markup problems revealed by the Zope 2.10 ZChecker
  tests.
  [hannosch]

- Moved css rules for the photo album view inside Plone's public.css,
  instead of having them inline in the template. This way they can be
  overridden. This closes http://dev.plone.org/plone/ticket/4765.
  [hannosch]

- Repaired the portal logo appearance visual bug in IE 5, 5.5.
  This closes http://dev.plone.org/plone/ticket/5228.
  [wald]

- Corrected the portlet_calendar view for tableless layout for Firefox.
  This closes http://dev.plone.org/plone/ticket/5467.
  [wald]

- When setting some background to the top, Live Search did not look
  properly. Moreover in IE it had a bad visual behavior. Changed the
  visual representation of the Live Search to repair the improper look.
  This closes http://dev.plone.org/plone/ticket/4313 and
  http.://dev.plone.org/plone/ticket/5005.
  [wald]

- contentActions drop down menus were falling below the content area text
  in IE. This closes http://dev.plone.org/plone/ticket/4949,
  http://dev.plone.org/plone/ticket/4960 and
  http://dev.plone.org/plone/ticket/4961.
  [wald]

- Updated tableless main_template.pt to get it in sync with the tablebased
  main_template.pt. This closes http://dev.plone.org/plone/ticket/5056.
  [hannosch]

- A confirmation page is now displayed upon successful submission of the
  contact-info form. This fixes http://dev.plone.org/plone/ticket/5301.
  [rocky]

- Added missing i18n translation in live search for 'Advanced search' and
  'Show all'. This closes http://dev.plone.org/plone/ticket/5425.
  [hannosch]

- Fixed incorrect coloring of workflow states in content menu in some
  cases, due to missing normalizeString call.
  This fixes http://dev.plone.org/plone/ticket/5078.
  [hannosch]

- Fixed typo in image_view_fullscreen.pt.
  This closes http://dev.plone.org/plone/ticket/5469.
  [hannosch]

- Fixed trivial error in validate_emailaddr.
  This closes http://dev.plone.org/plone/ticket/5249.
  [hannosch]

- External editor link showed on temporary content.
  This closes http://dev.plone.org/plone/ticket/5250.
  [hannosch]

- Calendar showed arrow when it's not clickable.
  This closes http://dev.plone.org/plone/ticket/5223.
  [hannosch]

- Links in calendar portlet showed only "published" items, rather than all
  states set by calendar tool.
  This closes http://dev.plone.org/plone/ticket/5077.
  [hannosch]

- OpenDocument files are no longer shown as garbage text. This fixes
  http://dev.plone.org/plone/ticket/5504
  [hannosch]

- Re-add a couple prematurely deleted scripts. Fixes #5482.
  [alecm]

- Fixes #5487.  Changed 'orig_template' query value from context's
  URL to HTTP_REFERER in 'object_rename' so that we can really
  redirect to the original view and not only the default view in
  'folder_rename'.
  http://dev.plone.org/plone/ticket/5487
  [maurits, nouri]

- Turn I(Selectable)ConstrainTypes and I(Selectable)Browser default into
  Zope 3 interface with reverse bridges. Depends on changes to
  ATContentTypes trunk and CMFDynamicViewFTI trunk as well!
  [optilude]

- Various small fixes for support of future CMF versions.
  [hannosch]

- Incorporate some fixes for Zope 2.10 support. Note that 2.10 is not
  officially supported for Plone 2.5.
  [hannosch]

- Deprecate CatalogTool._initIndexes
  [wichert]

- Add a category parameter to createToplevelTabs to allow skins to use a
  different action category.
  [wichert]

- The padding on the documentEditable content area depends on the design
  in public.css, and was moved there to make CSS customization more
  predictable.
  [limi]

- Fixed missing security declarations in MembershipTool.
  http://dev.plone.org/plone/ticket/5432
  [stefan]

- Allow turning off PlonePAS installation during 2.1 -> 2.5 migration
  using an environment variable.  If 'SUPPRESS_PLONEPAS_INSTALLATION' is
  'YES', then the migrations will not install PlonePAS.  This is not a
  supported configuration, but it should allow CMFMember/Teamspace users
  to upgrade their 2.1 sites.
  [alecm]

- No longer remove expires and effective parameters from catalog queries.
  The use of the DateRangeIndex is sufficient, no reason not to let users
  further restrict results.
  http://dev.plone.org/plone/ticket/4697
  [alecm]

- Use portal_transforms to do stx -> html conversion instead of relying
  on ugly module import in the quickinstaller configlet.
  http://dev.plone.org/plone/ticket/5428
  [alecm]

- Modify local role addition and removal scripts to only reindex object
  security once.
  http://dev.plone.org/plone/ticket/5352
  [wichert]

- Remove never used use_portrait handling from folder_localrole_set
  [wichert]

- Deprecate CMFPlone.MemberData. This class is never used, and the future
  is with PAS-based objects instead of membership/memberdata tools.
  [wichert]

- Marked FolderWorkflow and PloneWorkflow as deprecated. Workflow setup is
  handled by the GS profile now.
  [hannosch]

- Removed unused default configurations from PloneControlPanel and
  CatalogTool, which are handled by the GenericSetup profile now.
  [hannosch]

- Force a catalog reindex on upgrade to get correct work boundaries on
  transformed html content.
  http://dev.plone.org/plone/ticket/5393
  [wichert]

- Implemented displayContentsTab and getViewTemplateId in @@plone.
  The script getViewTemplateId is now deprecated, displayContentsTab
  will stick around for a while because people often override it in their
  content classes.
  [alecm]

- Added another convenience method to @@plone to simplify template
  and action logic.  getCurrentFolder() returns the object if it is a
  not the default page for its container and is a structural folder
  otherwise it returns the object's container.  Simplified some template
  and action logic.
  [alecm]

- Made all our deprecated scripts use the new views internally.
  [alecm]

- fix strange English in site feedback mail template. Fixes
  http://dev.plone.org/plone/ticket/5346
  [wichert]

- Added a cache decorator to the @@plone implementation so that multiple
  calls to expensive methods don't require multiple computations.
  [alecm]

- Added three convenience methods to @@plone to simplify action and
  template logic.  'getParentObject()', which returns the container of the
  current context object.  'isFolderOrFolderDefaultPage()', which returns
  True if the current object is either a folder or the default page of
  a folder.  'isPortalOrPortalDefaultPage()', which returns True is the
  current object is either the portal, or the default page of the portal.
  [alecm]

- Removed __getattr__ hack from the @@plone view.
  [alecm]

- introduce a large_site site property, which can be used to tweak site
  behaviour. Modify the user and group management templates to show all
  users and groups on small sites and search for them on large sites.
  [wichert]

- Fixed wrong html markup in events portlet.
  Closes http://dev.plone.org/plone/ticket/5407
  [hannosch]

- Fixed dumb migration issue bug http://dev.plone.org/plone/ticket/5357
  [alecm]

- Slightly optimized portlet events view for performance.
  [hannosch]

- Refactored some more logic out of portlet_calendar into calendar view.
  [hannosch]

- Removed vcXMLRPC.js.
  [fschulze]

- Removed underline button from Kupu, you shouldn't use underline for
  web pages - as it's very hard to discern from a link.
  If you want it back, add the following to your CSS file:
  #kupu-underline-button { display: inline; }
  [limi]

- Fixed up Summary View to show author/date on News Items and
  location/time on Events.
  [limi]

- Added condition so that you don't get the "send feedback to author" on
  yourself. If you don't know how to get in touch with yourself, seek
  professional help. ;)
  [limi]

- Disabled the RichWidget file upload field using CSS. The reason is that
  it causes a lot of problems for naive users, who upload Word documents,
  images etc here. The content has to be in HTML or the selected text
  format for this to work. If you want to re-enable this in your site, add
  the following to your CSS file: .fieldUploadFile { display: block }
  [limi]

- Removed inline styles on file upload field in RichWidget, added classes
  fieldUploadFile and fieldTextFormat so these elements can be styled
  using CSS.
  [limi]

- Adjusted status message related methods of PloneTool to the new
  implementation of statusmessages as an adapter for the request rather
  than a utility.
  [hannosch]

- Added some missing .metadata file for images.
  [panjunyong]

- Removed colophon.pt from the tableless skin - there's no need for it
  to have a separate file for this.
  [limi]

- Use fullname but not username in viewThreadsAtBottom.
  [panjunyong]

- Adding relaxed mode to PloneTool.normalizeString(). This will be used in
  ATContentTypes to avoid stripping too much from valid filenames being
  uploaded.
  [optilude]

- Making links link directly to the target in the navtree. Fixes
  http://dev.plone.org/plone/ticket/5264.
  [optilude]

- Making the user-name link in the personal-bar link to the author
  profile.
  Fixes http://dev.plone.org/plone/ticket/5268.
  [optilude]

- Added more insane TAL logic to portlets_fetcher.pt to actually show the
  error to the user, as opposed to simply logging it. If anyone has an
  issue  with this, please just remove the tal:on-error. Fixes
  http://dev.plone.org/plone/ticket/5282 and
  http://dev.plone.org/plone/ticket/2850.
  [optilude]

- Handle empty values for group properties of lines and ulines types
  correctly in the group details template.
  [wichert]

- Removed 'input' from the print CSS blacklist; forms print properly now.
  [limi]

- Moved the colophon icons into classes instead of using inline styles.
  [limi]

- Lots of improvements to the visual editor [limi]:

  - Added "pullquote" and "callout" layout classes, renamed "formatted"
    label to "literal"

  - Updating icons to better match the Plone style

  - Improved tool ordering (growing elements like the text format selector
    should be at the end, since they displace all the other icons when
    they change if not)

  - Fixed stupid bug in Mozilla by explicitly setting the link styling
    inside Kupu

  - Made all images load from an absolute URL to improve caching

- Fixed CSS regression: the p tag would sometimes be a victim of the
  peekaboo bug after we removed it to work better with Kupu; put it
  back in with a position: relative hack instead. This should work better.
  This closes http://dev.plone.org/plone/ticket/5225
  [limi]

- Made the file_view link directly to the file.
  This closes http://dev.plone.org/plone/ticket/5196
  [limi]

- The Sharing page was showing mail addresses to easier be able to discern
  between users with similar user names; now it uses full name instead.
  This closes http://dev.plone.org/plone/ticket/5196
  [limi]

- Move two IE hacks to IEFixes.css.dtml where there belong, as these had
  ugly side-effects when viewing a site with IE 7 beta2.
  [hannosch]

- Renamed "discussion" to "comments" in the UI, made the labels more
  explicit about what they actually do.
  [limi]

- Checkboxes got background in IE, this was fixed. Also moved the
  'noborder' class to public.css.
  [limi]

- prefs_mailhost_form looked up "smtp_server" in a strange location.
  Removed some backwards compatibility code from PropertiesTool as well.
  Fixes http://dev.plone.org/plone/ticket/5174.
  [hannosch]

- Clarify description for 'show short name' feature in the prefs panel.
  Closes http://dev.plone.org/plone/ticket/5112.
  [hannosch]

- Added warning message to version overview in the control panel if PIL
  is not installed. Closes http://dev.plone.org/plone/ticket/5134.
  [hannosch]

- Fixed inconsistencies where some 'Controller Python Script' were being
  declared as normal 'Script (Python)' and were missing the state
  variable.
  [deo]

- Fix confusion between user names and user ids in the membership tool.
  Fixes http://dev.plone.org/plone/ticket/5098
  [wichert]

- Fixed bug: can't access content when the user have no permission to
  access the acquired left_slots/right_slots properties.
  [panjunyong]

- Introduced a new class "tile" to use in the portlets. The previous
  portlet code implicitly assumed that all links would be block-level,
  which is not a good thing. This should have minimal impact on old
  portlets, but if you want the block-level behaviour and stay compatible
  with older portlet code too, just add class="tile" to your links.
  [limi]

Beta 1 - released March 31, 2006

- Added "Extension profile" support to the addSite.zpt ZMI form to allow
  extension profiles to be applied to a site at site creation time,
  similar to how customization policies used to be available.
  [rafrombrc]

- Removed nearly all instances of the "classImplements" idiom which
  dynamically creates Z3 interfaces from Z2 interfaces, replaced them
  with real Z3 interfaces, dynamically creating Z2 interfaces using
  "createZope3Bridge" calls.
  [rafrombrc]

- Fixed up Summary View to show author/date on News Items and
  location/time on Events.
  [limi]

- Incorporated various fixes for RTL support.
  http://dev.plone.org/plone/ticket/5299
  [fschulze]

- Moved the hidden accessibility items from public.css to base.css.
  [limi]

- Finally put back the native support for rounded corners that was pulled
  out right before the 2.1.0 release, you can now put rounded corners on
  portlets by using the portlet(Top|Bottom)(Left|Right) classes.
  [limi]

- Fixed duplicate css definition for livesearch background. This fixes
  http://dev.plone.org/plone/ticket/5366.
  [hannosch]

- Fixed erroneous form actions in prefs_error_log_form. Made it work even
  if the button labels were translated.
  [hannosch]

- Tabindexes aren't as good for usability/accessibility as we once
  thought, and they wreak havoc with JavaScript/AJAX type code that
  dynamically inserts form elements. Instead, we should have the first
  element in the main body have tabindex="0" and the rest not have
  tabindexes, this making the cursor focus on that element first, and then
  follow normal ordering thereafter. Fixed IndexIterator to support just
  this - when mainSlot=False it always returns None; when mainSlot=True,
  it returns a number on the first iteration, and no number thereafter.
  Fixed up global_defines, the portlet fetcher and various templates that
  were abusing tabindexes to get a unique number for form elements to
  reflect this. Also added a new iterator called uniqueItemIndex in
  global_defines, which can be used when a page-unique number *is* needed,
  as it is in calendar_macros.pt.
  [optilude]

- Replace &larr; with '-' in the breadcrumb trail for RTL environments. It
  seems that &larr; is not present in common RTL fontsets on Windows.
  Firefox can compensate for that, but IE can not.
  http://dev.plone.org/plone/ticket/4388

- Re-added toPortalTime script which was accidentally removed earlier. It
  is deprecated though and won't be included in Plone 2.5. This closes
  http://dev.plone.org/plone/ticket/5326.
  [hannosch]

- Added explanatory doctests for the translation service tool l10n
  methods.
  [hannosch]

- Added some missing i18n statements for link related tags in the headed.
  This fixes http://dev.plone.org/plone/ticket/5289.
  [hannosch]

- Fixed exception in getDefaultPage when the LinguaPlone-aware content
  type is not associated with a workflow chain.
  [panjunyong]

- Added Turkish map for UnicodeNormalizer and consolidated the mappings.
  This fixes http://dev.plone.org/plone/ticket/5292.
  [hannosch]

- Included e-mail address in mail_password_form into the i18n message.
  Fixes http://dev.plone.org/plone/ticket/5045.
  [hannosch]

- Modified viewThreadsAtBottom to make it better work with css:
  div is not shown when no discussions exist or no discussions
  are allowed. Image icons in front of each reply is now a background
  image so that can also be styled by css alone. Added the style in
  authoring.css
  [ender]

- Standardized how description fields are rendered in html among the
  various templates. document_view used a <p> while folder_listing
  used a <div> etc. They all use <p> now and omit the field completely
  when there is no description (all similar to document_view).
  [ender]

- Re-added support for topLevel and bottomLevel navtree properties, as
  well as the new name (of the navtree portlet) and root (of site
  navigation) properties, and added the Sprout navtree preference panel to
  let users manage these settings. Factored the navtree code out to
  .browser.navtree, which is TTW importable and contains a reusable
  buildFolderTree() function that can be used to build navtree-like
  structures in custom code. See the docstrings in that module for more
  details.
  THIS REQUIRES THAT YOU RE-CUSTOMIZE YOUR NAVTREE IF YOU HAVE A CUSTOM
  VERSION IN YOUR SITE!
  Fixes http://dev.plone.org/plone/ticket/5265.
  [optilude]

- Split the various navigation views into their respective parts, no more
  meta-navigation interface.
  [alecm]

- Do no use javascript in failsafe_login_form - it is not safe
  [wichert]

- Remove use of zLOG in favor of the python logger, add some content
  classes to five:deprecatedManageAddDelete to avoid some warnings.
  [alecm]

- Added a BBB getMultiAdapter to lookup views for zope 2.8, which means
  fewer deprecation warnings and an easier migration path to zope 2.10.
  [alecm]

- Added getEventType index for KeywordWidget in the ATCT event type.
  [fschulze]

- Added method to Catalog Tool to fully rebuild the catalog by walking the
  tree and looking for content, as well as a ZMI button.
  Fixes http://dev.plone.org/plone/ticket/4438
  [alecm]

- Removed code from Portal.py for default_frontpage. This is now handled
  by the GenericSetup driven site creation. This fixes
  http://dev.plone.org/plone/ticket/5332
  [hannosch]

- check_id error messages were not translated. This fixed
  http://dev.plone.org/plone/ticket/5012
  [hannosch]

- Added view for sitemap, and made navtree use a recursive macro call,
  rather than recursively calling the template, as it should be faster.
  Fixes http://dev.plone.org/plone/ticket/5240
  [alecm]

- Added drag'n'drop reordering of folder contents.
  [fschulze, alecm]

- Fix PloneTool.changeOwnershipOf to not test for user existence by
  trying to find a user id in listMemberIds().
  [wichert]

- Remove options to list all members and groups from the preference pages;
  this does not scale and may not be possible in PAS environments.
  [wichert]

- Merge PlonePAS skin layer into CMFPlone skin
  [wichert]

- Rewrite ownership_form to not list all users, but allow searching for
  possible new owners instead.
  [wichert]

Alpha 2 - released February 23, 2006

- Major refactoring of the entire PloneGenerator / portal creation
  framework; now using GenericSetup with XML-based setup profile to
  specify the initial site configuration state. (see
  CMFPlone/profiles/default directory)
  [rafrombrc]

- Added ignoredSkinLayers option to zcheck.py to filter out certain
  folders.
  [hannosch]

- Removed default front-page from ./www. New location is:
  ./profiles/default/structure
  [hannosch]

- Merged PlonePAS bundle. This implements the start of step 2 for PLIP
  102.
  [wichert]

- Do no list all groups in the sharing screen, but make it possible to
  search for them. Fixes (last) part of
  http://dev.plone.org/plone/ticket/2530
  [wichert]

- Fix confusion between user names and user ids in the membership tool.
  Fixes http://dev.plone.org/plone/ticket/5098
  [wichert]

- Converted unit tests to use the external PloneTestCase product instead
  of a local modified copy.
  [hannosch]

- Factored out 'default page'-related functionality into a view
  that provides IDefaultPage. Factored out createBreadCrumbs into
  a view that provides INavigationStructure. Started implementing
  soon-to-be-written PLIP for configurable navigation root.
  [sidnei]

- Factored out most of the 'functions' in PloneTool.py into real
  functions that take a 'context' in utils.py. Later one, those
  will be used by the new adapters code.
  [sidnei]

- Added helper functions for making 'zope.interface'-style
  declarations from Zope 2 interface declarations. Removed some
  BBB code. Make sure that for all interfaces declared, they are
  declared for both Zope 2 and 'zope.interface'-style.
  [sidnei]

Alpha 1 - released January 29, 2006

- Installed CMFPlacefulWorkflow during migrations.
  [encolpe]

- Merged plip108-five-translationservice r8093:8841 into trunk.
  This implements PLIP 108 Zope3 MessageID's and PLIP 111 new portal
  status message infrastructure.
  [hannosch]

- Merged hannosch-cleanup branch. This removes a lot of unused files and
  moves some files to /portal_skins/plone_deprecated which will be removed
  in the next release.
  [hannosch]

2.1.5 - Fischerspooner - (Unreleased)
-------------------------------------

- Fixed handling of login_time and last_login member properties:
  last_login_time is now the time of the previous login and login_time is
  the time of the current login. This fixes
  http://dev.plone.org/plone/ticket/5965.
  [hannosch]

- Fixed the sharing page to handle groups which come from non-traditional
  PAS sources. This closes
  http://dev.plone.org/plone/ticket/5727.
  [hannosch]

- Fixed the view of livesearch in fullscreen mode (contentActions were
  overlapping the livesearch output).
  [spliter]

- Enabled IEFixes.css for all IE's, not for <IE7 only
  [spliter]

- Re-enabled livesearch back (removed overflow:hidden from
  #portal-searchbox) and fixed horizontal scroll issue for IE's due to
  floated searchbox.
  [spliter]

- Removed www/main.dtml as it turns out we can use the default just fine.
  [stefan]

2.1.4 - Devo - Released September 19, 2006
------------------------------------------

- No changes since RC1.

   RC1 - Released September 12, 2006

- Made sure validate_email is turned on by default.
  [stefan]

- Fixed a bug in the highlighting of selected tabs in an environment which
  uses Apache rewrite rules. This closes
  http://dev.plone.org/plone/ticket/5518.
  [hannosch]

- Updated the CSS validation link to use the CSS 2.1 and CSS 3 compatible
  profile, which is what Plone uses.
  [limi]

- Using 'indexObject' instead of 'reindexObject' for
  CatalogTool.clearFindAndRebuild works just as well, but does not
  touch every object and cause a monster transaction to be committed.
  Also improved the ZMI experience.
  [stefan]

- Rearranged some of the nav tree CSS so it is easier to have proper
  padding when not using the icons.
  [limi]

- Made the local nav tree functionality better, has correct indentation
  now.
  [limi]

- Minor spelling fix in folder_localrole_form.
  [hannosch]

- Removed OS notes for iCal and vCal on the event view. Meanwhile both
  standards are used on all OS'es. This closes
  http://dev.plone.org/plone/ticket/4113.
  [hannosch]

- Fixed mysterious RuntimeError bug in rssAllowed.py.
  This closes http://dev.plone.org/plone/ticket/5611.
  [hannosch]

- Use Fullname in recently_published and modified templates
  [jladage]

- Cleaned up some messages that were only differing slightly.
  [hannosch]

- Changed remaining blank 'a' styles to 'a:link' to make sure anchors aren't
  affected.
  [limi]

- Fix rename from the action menu when using virtual hosting. Thanks to
  Daniel Nouri, Maurits van Rees, Alec Mitchell and Stefan Holek for
  pointers and code.
  [optilude]

- Added plone.css Python Script that returns the rendered CSS for use when
  external tools need a static reference. Cached for one day.
  [fschulze][limi]

- Added portal status message to author and personalize_form. Since Limi
  Added the tabs and switched to the content slot instead of main, the
  status message wasn't shown.
  [jladage]

- Fixed Plone/Unknown in HTTP Server header. It now shows the correct
  Plone version (again).
  [stefan]

- Changed the default background color to match the defined background
  color for better readability. If you want the old behaviour back, add
  'dl.portlet { background-color: transparent }' to your style sheet.
  [limi]

2.1.2 - Saint Etienne - Released January 20, 2006
-------------------------------------------------

- Events portlet was not displayed when /events had been deleted.
  Closes http://dev.plone.org/plone/ticket/5143.
  [hannosch]

- Reinstating the "Previous Events" link in the events portlet (was
  removed in r7864)
  [limi]

- Removing hardcoded style attributes in folder_localrole_form.
  This fixes #5070.
  http://dev.plone.org/plone/ticket/5070
  [limi]

- Removed useless CSS declaration in generated.css - the site map
  will never have a current item by its very nature. This fixes #5079.
  http://dev.plone.org/plone/ticket/5079
  [limi]

- Made Plone notify you when you are trying to log out while being
  logged in via HTTP (you need to close your browser to log out when
  using HTTP auth). This also fixes #5083.
  http://dev.plone.org/plone/ticket/5083
  [limi]

- Fixed the non-workflow-state-dependend coloring of items in the
  navigation portlet. Closes http://dev.plone.org/plone/ticket/5136.
  [hannosch]

- Changed the last occurrences of transaction.commit(1) to new style
  transaction.savepoint(optimistic=True) calls.
  [hannosch]

- Removed the last remaining occurrences of CMFCorePermissions.
  [hannosch]

- Updated deprecation warnings to reflect new version numberings.
  [hannosch]

- Fixed some minor spelling mistakes and i18n / xhtml format issues.
  [hannosch]

- Added missing migration of PortalTransforms to activate the
  new, configurable safe_html transformation.
  [stefan]

- Add a folderlistingFolderContents method to the PloneSite type. This
  allows getting folder contents with the AccessContentsInformation
  permission and is required by ATReferenceBrowserWidget since its
  changeset 5440. Fixes http://dev.plone.org/plone/ticket/5115
  [wichert]

- Remove more uses of the name CMFCorePermissions by using
  CMFCore.permissions throughout the code.
  [wichert]

   RC2 - Released January 5, 2006

- Error when trying to force migrate to 2.1.2 from 2.1.1 due to non-failsafe
  addition of memberdata property. http://dev.plone.org/plone/ticket/5064
  [hannosch]

   RC1 - Released January 4, 2006

- Home page edit field was missing from the author edit screen, added.
  [limi]

- Added missing class="documentContent" declarations in the user management
  screens.
  [limi]

- Added View/Edit tabs to the author profile screen to make it easier to
  change your own details.
  [limi]

- Changed the 'expired' color to be the same as the discreet/ghosted
  elements, since this is a marker to show content that is no longer
  active, not content that needs some sort of action.
  [limi]

- Moved .visualClear to the base.css - even though it's not an actual tag,
  all layouts break without this present, so makes sense to have it as a
  base-level element.
  [limi]

- Added link to "Advanced Search" in the LiveSearch pulldown.
  [limi]

- Moved .documentContent to 'public.css', this fixes #5061.
  http://dev.plone.org/plone/ticket/5061
  [limi]

- More CSS grouping fixes: the form elements are visible in the public
  view, and were moved to 'public.css' (were previously in 'authoring.css')
  [limi]

- Moved the accessibility CSS classes from 'authoring.css' to 'public.css'
  (the hiddenStructure classes).
  [limi]

- Moved the collapsible CSS class from 'public.css' to 'authoring.css',
  where it belongs.
  [limi]

- Added background tint to inputs and textareas.
  [limi]

- Fixed a bug in FactoryTool were objects weren't removed from the UID and
  refs catalogs after changes introduced in Archetypes 1.3.6.
  [hannosch]

- Permission check had wrong spelling in prefs_groups_overview, this fixes
  #5055. Thanks to Bertrand Mathieu for the patch.
  http://dev.plone.org/plone/ticket/5055
  [limi]

- Added feedButton class for RSS feed buttons. This will be used for e.g.
  the news portlet once limi bothers to put them back in.
  [optilude]

- Escape the group name URLs generated in the group preferences screen.
  http://dev.plone.org/plone/ticket/5015
  [wichert]

- Added some classes for the RTL versions of the summary view. Thanks,
  mohsen.
  http://dev.plone.org/plone/ticket/5047
  [limi]

- Fixed #4976 - Added a must_change_password property to the
  member data (set to 0 for existing members).
  http://dev.plone.org/plone/ticket/4976
  [plonista]

- Fixed various log-in problems, issues #4545, 4975, 4942, added workaround
  that should prevent problems in #4482 and #4688.
  [plonista]

- Login UI cleanup. Now redirect directly to came_from page after login if
  we can verify that the user has cookies enabled via javascript. Added
  login_name to query string in a few places to save some typing. Only show
  the newbie text the first time somebody logs in.  Add a login shortcut
  link to the new user email. Tell people to enable javascript if they don't
  have it enabled.
  [plonista]

- Update all skin form scripts to fetch transaction_note from the correct
  location (Products.CMFPlone.utils)
  [wichert]

- Portlet CSS simplification - portletItemSingle and portletItemLast are
  no longer needed. They are still supported via the deprecated.css file,
  but we urge people to adopt the new style (which is much simpler and
  more flexible) - as the inclusion of the two above classes in the 2.1
  release was not intentional.
  http://dev.plone.org/plone/ticket/4430
  [spliter, limi]

- Fixed #5041 - plone-site icon is generated again. Thanks, optilude ;)
  http://dev.plone.org/plone/ticket/5041
  [spliter]

- Fixed #4961 - long Titles have been overlapping documentActions in IE.
  http://dev.plone.org/plone/ticket/4961
  [spliter]

- Fixed #5020 - added wrapping SPAN's in portlets' portletHeaders to allow
  css designers to use rounded corners techniques.
  http://dev.plone.org/plone/ticket/5020
  [spliter]

- Quote id in "Move item up" and "Move item down" links.
  http://dev.plone.org/plone/ticket/5014
  [nouri]

- Removed leading whitespace in portlet_navtree_macro css class definitions.
  http://dev.plone.org/plone/ticket/5038
  [hannosch]

- Fixed author.pt to respect search type blacklisting.
  http://dev.plone.org/plone/ticket/5034
  [hannosch]

- Fixed 4876 by making Discussion Item not have a workflow, so that you
  won't get strange permission inconsistencies.
  http://dev.plone.org/plone/ticket/4876
  [optilude]

- Fixed 3905 by making mergeResults() available TTW to allow python scripts
  to merge search results.
  http://dev.plone.org/plone/ticket/3905.
  [optilude]

- All-new look for the photo album / thumbnail view.
  [limi]

- Extended tests to ensure publishing of included folders is working.
  http://dev.plone.org/plone/ticket/4933
  [hannosch]

- Fixed #5021 - 'History' being expanded was visible through the vertical
  table, containing event's summary
  http://dev.plone.org/plone/ticket/5021
  [spliter]

- Fixed #4430 - now portlets have much more simple and straightforward
  structure and styles. From now we use only three classes for them -
  portletHeader, portletItem and portletFooter. Thanks to mroch for idea.
  http://dev.plone.org/plone/ticket/4430
  [spliter]

- Backported some general code cleanup from the trunk.
  [hannosch]

- Implemented new feature: Automatically highlight keywords when arriving
  from search engines.
  http://dev.plone.org/plone/ticket/2599
  [jenner] [hannosch]

- Made prefs_mailhost_form compatible with regular mailhost objects from
  both Zope 2.7 and 2.8. Starting with 2.8 MailHost has user/pwd attributes
  as has SecureMailHost but named slightly different.
  http://dev.plone.org/plone/ticket/5000
  [hannosch]

- LiveSearch did not match 8-bit search strings correctly.
  http://dev.plone.org/plone/ticket/4643
  [hannosch]

- Added a customised testPropertiesValidity method to the RegistrationTool
  in preparation of PAS. This version only verifies the email property if
  it is writable.
  [wichert]

- Fixed #5013 - accessibility-page had a problem in CSS validation due to
  doubled #portal-siteactions. Now it is the class because we have more than
  one place for siteactions on the pages.
  http://dev.plone.org/plone/ticket/5013
  [spliter]

- Fixed #5017 - Unnecessary style in IEFixes.css that ruined NewsItem view
  in IE when having paragraph in text.
  http://dev.plone.org/plone/ticket/5017
  [spliter]

- Fixed 'Livesearch can kill a server' problem by enabling livesearch only
  for two or more characters long search strings.
  http://dev.plone.org/plone/ticket/4890
  [hannosch]

- Fixed two problems with delete action in global_contentmenu.
  'Cannot cancel deletes in IE 6' (#4772) and 'JS pop-up shows wrong type
  when deleting default view' (#4990).
  http://dev.plone.org/plone/ticket/4772
  http://dev.plone.org/plone/ticket/4990
  [hannosch]

- Bug in portlet_navigation - navTreeLevel1 was never set.
  http://dev.plone.org/plone/ticket/4950
  [hannosch]

- Group is confused with identical user when trying to add as a subgroup.
  http://dev.plone.org/plone/ticket/4947
  [hannosch] [csenger]

- Fixed weak-ass tests that failed to catch broken action providers.
  Also fixed ActionsTool so it ignores broken providers.
  [stefan]

- Icon for links was missing padding in folder_listing. Fixes #4721.
  http://dev.plone.org/plone/ticket/4721
  [limi]

- Meta tags were not being emitted correctly. This fixes #4810.
  http://dev.plone.org/plone/ticket/4810
  [limi]

- Changed all calls to getParentNode() to be aq_inner.getParentNode() to
  make it work better with Five. This fixes #4705.
  http://dev.plone.org/plone/ticket/4705
  [limi]

- Review history was not valid XHTML, a block-level element was nested
  inside an inline element. This fixes #4926 and #4586 (hopefully, seems
  to work in my local testing).
  http://dev.plone.org/plone/ticket/4926
  http://dev.plone.org/plone/ticket/4586
  [limi]

- Made the "click here to see full size image" and size text on images
  invisible when printing the image. This fixes #4698.
  http://dev.plone.org/plone/ticket/4698
  [limi]

- Harmonized table-less and table-based skin, the former was using a special
  getBodyTagClass which has an existing equivalent in the normal skin anyway.
  Deprecated the special file used for this, it will disappear in Plone 2.5.
  This fixes #3915.
  http://dev.plone.org/plone/ticket/3915
  [limi]

- Inserted missing conditional check for the location of an event - no
  longer shows the location field if it has no value.
  [limi]

- Fixed #4695 - Comments were connected to the wrong object.
  http://dev.plone.org/plone/ticket/4695
  [morphex]

- Fixed #4998 - Russian characters were not supported by normalizeUnicode.
  Thanks to Xenru.
  http://dev.plone.org/plone/ticket/4998
  [stefan]

- Fixed the Internet Explorer visual bug where portlets would gradually
  lose their left margin and move further and further to the left the more
  elements were contained inside the portlet.
  http://dev.plone.org/plone/ticket/4874
  [limi]

- Fixed #4996 - favorites_view.pt had duplicated calls for
  'document_actions' macros.
  http://dev.plone.org/plone/ticket/4996
  [spliter]

- Plone was showing the editable border on all content items when you were
  logged in as a Member. This was fixed by removing the check for
  'Copy or Move' in the code that determines whether the editable border
  should be rendered.
  [limi]

- Fixed #2295 - text on printing was cropped on the right in all browsers
  when the tableless layout is used.
  http://dev.plone.org/plone/ticket/2295
  [spliter]

- 'external_edit' link wouldn't work for files with spaces in name due to
  use of 'url_quote_plus'. The correct function to use is 'url_quote'.
  [sidnei]

- Fixed #4859 - strftime error in calendar_macros.pt.
  http://dev.plone.org/plone/ticket/4859
  [hannosch]

- Fixed #3268 and #3746 - some status messages included all changed objects
  which could break IE as it supports only a limited URL length.
  http://dev.plone.org/plone/ticket/3268
  http://dev.plone.org/plone/ticket/3746
  [hannosch]

- Replacing all references to "portal" in the UI with "site" with same
  consequences as outlined below.
  [limi]

- Replacing "Member" with "User" everywhere in the UI (except in words like
  "membership"). Hanno has been notified, and this should not have any
  impact for i18n people, but they should be notified in case they made a
  distinction between member and user in their translations. I know most
  translations I have seen didn't.
  [limi]

- Added CMFPlone.utils._unrestricted_rename() by copying from ATCT
  migrations. _unrestricted_rename() allows to rename objects without
  going through _verifyObjectPaste().
  [stefan]

- Fixed #4657 and #4829 - wrong icon path in livesearch.
  http://dev.plone.org/plone/ticket/4657
  http://dev.plone.org/plone/ticket/4829
  [hannosch]

- Added PIL version to control panel version overview as suggested in #4775.
  http://dev.plone.org/plone/ticket/4775
  [hannosch]

- Fixed #4803 and #4943 by only deleting existing text indexes when the
  lexicon is missing (e.g. when we actually have a new catalog being
  created).
  http://dev.plone.org/plone/ticket/4803
  http://dev.plone.org/plone/ticket/4943
  [alecm]

- Fixed #4898 - migrations would break if the Plone Site was configured to
  not allow all content types.
  http://dev.plone.org/plone/ticket/4898
  [stefan]

- Fixed #4951 by overriding the 'sl' global define in prefs_main_template.pt
  http://dev.plone.org/plone/ticket/4951
  [alecm]

- Updated favorites portlet to the new portlet style.
  [ctheune]

- Fixed #4800 - hardcoded review_state variable breaks custom workflows.
  http://dev.plone.org/plone/ticket/4800
  [hannosch]

- Fixed #4938 - member portraits were referenced using the username instead
  of the member id in a few places in the membership tool.
  http://dev.plone.org/plone/ticket/4938
  [wichert]

- Combined the support for publishing subobjects in
  content_status_history.cpt with the support for bulk publishing. The old
  behaviour showed, but didn't use, the checkbox for publishing subobjects
  when you published a folder directly.
  [ctheune]

- Send correct password in the registry notification mail even if the stored
  password are encrypted.
  [panjunyong]

- Updated externalEditorEnabled.py to comply with WebDAV changes in
  Archetypes 1.3.6.
  [hannosch]

- Fix unit test relying on user folder storing passwords in plain text. This
  isn't anymore the default for Zope 2.9. Changed to test authenticate.
  [hannosch]

- Some code cleanup, mainly removal of unused imports.
  [hannosch]

- Fixed #4894 - Missing closing quote in LiveSearch pop-up.
  http://dev.plone.org/plone/ticket/4894
  [stefan]

- Send new generated plain password via email directly when reset password,
  but not the one stored in userfolder since it could be encrypted. Also use
  getProperty to retrieve email address for better LDAP integration.
  [panjunyong]

- Made plonifyAction be called with an existing default_tab parameter.
  [deo]

- Changed selectedTabs.py to use full URL instead of content path when
  computing whether or not a portal_tab action is being viewed. This causes
  portal tabs to behave correctly when the action refers to a specific
  template.
  [rafrombrc]

- Removed skins/plone_3rdParty/CMFTopic from filesystem and written
  migration to remove it from all skins.
  [hannosch] [limi]

- Removed unused errorMessages.py script.
  [hannosch]

- Removed some BBB code for Zope 2.6 (try/except on DateTimeError).
  [hannosch]

- Added accessibility instructions for Konqueror.
  [limi]

- Remove so called 'ie7' from third party skins and all references to it.
  [limi] [hannosch]

- Make Plone 2.1 degrade more gracefully on a non-migrated 2.0 site
  (special fixes for plone.org).
  [sidnei]

- Fixed #4788 - Missing i18n for livesearch 'no matching results found'.
  http://dev.plone.org/plone/ticket/4788
  [hannosch]

- Fixed small bug in searching users from prefs_users_overview. In case of
  searchstring field contained something, click to 'Find all' does not find
  all users, but only users specified by the search string.
  [naro]

- Changed folder_contents.pt so that it honors the
  'typesUseViewActionInListings' setting in site_properties for ALL types
  (was only working for non-folderish types before).
  [rafrombrc]


2.1.1 - Coloma - Released October 13, 2005
------------------------------------------

- Made the ExtendedPathIndex migration apply to all EPI from any ZCatalog
  instance in the portal root.  Should fix issues with migrating CMFMember
  instances.
  [alecm]

- Fixed #4587 - workflow history displays author's full name instead of
  author's id and link to author page instead of home folder (to be in sync
  with document byline). Added colored transition names as a free bonus.
  http://dev.plone.org/plone/ticket/4587
  [naro]

- Fixed #4690 - user can't change password after initial login
  (with 'validate email' set).
  http://dev.plone.org/plone/ticket/4690
  [naro]

- Fixed #4777 - 'portlet_navtree_macro_opt' call in sitemap.pt.
  http://dev.plone.org/plone/ticket/4777
  [hannosch]

- Fixed #4722 the SecureMailHost migration was test-free and not very
  cautious.
  http://dev.plone.org/plone/ticket/4722
  [alecm]

- Refixed #4639 by checking the presence of the property without acquisition
  and then using it only if it exists on the object, but allowing full
  acquisition if the property is there.
  http://dev.plone.org/plone/ticket/4639
  [alecm]

- Added migration to the new ExtendedPathIndex structures.
  [alecm]

- Fixed #4760 by making our GroupsTool reindex the group folder when it is
  newly created.
  http://dev.plone.org/plone/ticket/4760
  [alecm]

- Fix DeprecationWarnings resulting from CMFCorePermissions imports by
  importing from new permissions modules instead.
  [hannosch]

- Fixed #4766 - RSS feed in Firefox did not work properly.
  http://dev.plone.org/plone/ticket/4766
  [naro]

- MimetypesRegistry wasn't correctly handling 'globs' from shared-mime-info
  database, resulting in failure from detect correct mimetype based on
  extension on Windows platform. A migration was added to fix existing
  MimetypesRegistry instances.
  [sidnei]

- Added first migration to 2.1.1.
  [sidnei]

- Fixed #4704 - string.whitespace is not ASCII only on OpenBSD, which
  resulted in problems in UnicodeNormalizer.
  http://dev.plone.org/plone/ticket/4704
  [hannosch]

- Fixed #4708 - portlet_events "upcoming events" link broke if events folder
  was renamed or deleted.
  http://dev.plone.org/plone/ticket/4708
  [hannosch]

- Fixed #4755 - folder_factories does not link to folder_constraintypes_form
  like add item menu does.
  http://dev.plone.org/plone/ticket/4755
  [hannosch]

- Removed out-of-the-box TextIndexNG2 support from Plone. TextIndexNG V2 and
  V3 has explicit migration code to convert ZCTextIndexes to TextIndexNG
  V2|3 instances on request. This fix should resolve bug #4713.
  http://dev.plone.org/plone/ticket/4713
  [ajung]

- Fix broken discussion_reply_form.cpt.
  [hannosch]

- Reverted some non-literal msgids introduced in Python code to literal
  msgids as i18ndude is not capable of handling these right now. We'll have
  to wait for Zope3-style MessageID's.
  [hannosch]

- A number of micro-optimizations.  The biggest winners are precompiling
  the regexes used in normalizeString at startup, and switching the
  navtree to use a recursive macro rather than recursively calling a
  page_template.  The rest of the changes involve making sure that the
  global_defines are used rather than being re-executed/acquired, and
  removing repeated attempts to acquire the same object in a tal:repeat.
  Added two new global defines, one for the normalizeString method, which
  is used very frequently (usually in loops) so that the method lookup is
  avoided, and another for isViewTemplate which uses an expensive script
  which was being called twice per page.
  [alecm]

- Optimizing normalizeString slightly by moving a list concatenation out of
  the methods scope.
  [hannosch]

- Significantly speed up toLocalizedTime calls. We try to get the needed
  format identifiers first and only calculate the real values for those
  instead of calculating all values on every call. This safes a lot of
  quite expensive DateTime.strftime() calls.
  [hannosch]

- Corrected lots of conflicting (swallowed) default texts for i18n msgids.
  Found by new i18ndude feature.
  [hannosch]

- Removed unnecessary use of 'SESSION' in 'folder_contents' and
  'logout_form'.
  [sidnei] [alecm]

- Converted plone_javascript_variables.js from DTML to PageTemplate to make
  it better suited for i18n.
  [fschulze]

- Cleaning up markup around i18n:name with tal:omit-tag="" to prevent
  double span tags and some general markup improvements.
  [hannosch]

- Fixed calendar portlet to show abbreviated weekday names when no
  translation service is available.
  [alecm]


2.1 - Plaid - Released September 6, 2005
----------------------------------------

- Added deprecation warning for DTML in CSS. We will most likely get rid
  of this in Plone 3.0 or 4.0 to reduce complexity. If we are going to
  support variables in CSS, ResourceRegistries should handle it, not DTML.
  [limi]

- Fixed #4639 by using aq_explicit instead of aq_base when getting Title for
  pretty_title_or_id. This means that objects which rely on acquisition in
  their Title() methods will need to do so explicitly, though getToolByName
  and aq_parent will work without issue.
  http://dev.plone.org/plone/ticket/4639
  [alecm]

- A bug that caused the month display to use the day number was fixed.
  Thanks to Mohsen Moeeni for finding this bug.
  [longsleep]

- Fixed #4638 by making the workflow title methods more fault tolerant.
  http://dev.plone.org/plone/ticket/4638
  [alecm]

- Fixed #4624 - document byline on events were not translated.
  http://dev.plone.org/plone/ticket/4624
  [hannosch]

- Fixed #4635 - LiveSearch background did not apply the IE fix if there was
  no result set. Thanks Wichert.
  http://dev.plone.org/plone/ticket/4635
  [limi]

- Fixed #4612 by granting the 'View Groups' permission to all Members at the
  portal root.
  http://dev.plone.org/plone/ticket/4612
  [alecm]

- Fixed #4589 by adding some tal:conditions in a few templates.
  http://dev.plone.org/plone/ticket/4589
  [alecm]

- Reordered the object button actions.
  [alecm]

- Removed the printing of link addresses along with the link text since it
  triggers a lot of display-related bugs when printing certain types of
  documents. Left the code in there, so just uncomment it if you want the
  feature back. Too painful for the generic use case, though.
  [limi]

- Removed the "blah's Home" title for the member folder default title. It
  doesn't make sense in multilingual sites, and doesn't add any useful
  information. The home folder now has a title that is simply the username.
  [limi]

- Enabled editable border for the Members folder.
  [limi]

- Provide compatibility with Five 1.1 regarding i18n. Five's
  TranslationService has no unicode aware utranslate method, so we have to
  force a fallback to PTS or everything using utranslate including
  ulocalized_time won't get translated.
  [hannosch]

- Provided descriptive titles for translation_service, mimetypes_registry,
  and portal_transforms tools.
  [stefan]

- Login and saving of login times now also works if members do not have the
  "Set own properties" permission.
  [stefan]

- Made sure that if you have an INonStructuralFolder inside another, you
  don't get an add menu for the parent non-structural folder.
  [optilude]

- Made sure the cmf_legacy skin layer comes last, after all the Plone
  layers.
  [stefan]

- Added Kupu image alignment classes. Thanks, Nate.
  [limi]

- Fixed various spacing issues in discussions rendering.
  [stefan]

- In skins/plone_login/logout.cpy, $-quoted a string that was being taken
  from REQUEST and inserted into a TALES 'string:' expression. This REQUEST
  string could be manipulated by the browser.
  [rochael]

- Fixed #4530 - type name not translated if only one type is shown in
  global_contentmenu.
  http://dev.plone.org/plone/ticket/4530
  [hannosch]

- Adding some padding to the "display" menu header if the menu is disabled
  because of an index_html document. Closes #4534.
  http://dev.plone.org/plone/ticket/4534
  [optilude]

- Made Summary View the default view for the news topic.
  [alecm]

- Fixed #4499 - removed vestigial failsafe_login.pt.metadata.
  http://dev.plone.org/plone/ticket/4499
  [hannosch]

- Fixed #4484 - 'My Preferences' action title is 'Preferences' in 2.1.
  http://dev.plone.org/plone/ticket/4484
  [hannosch]

   RC3 - Released August 18, 2005

- Changed the copy action to be restricted by 'View' as 'Copy or Move' is
  generally available to anonymous even when 'View' is not.
  [alecm]

- Fixed #4502 by reverting to the old nasty deprecated _usage method of
  doing things.  This should be cleaned up once zope 2.7.8/2.8.2 comes out
  and make_query is fixed. queryCatalog automatically converts the _usage
  style queries into proper dict based queries, but it's still bad form.
  http://dev.plone.org/plone/ticket/4502
  [alecm]

- At the request of the i18n team I renamed Tile View to Summary View,
  since this is easier to translate.
  If you are running an SVN checkout between RC2 and RC3, please re-run
  migrations from RC2 to get the right template name and reference.
  [limi]

- Added explicit permission checks to prefs_users_overview and
  prefs_groups_overview to prevent unnecessary exposure of sensitive
  roles and groups security information (see #4491).
  http://dev.plone.org/plone/ticket/4491
  [rafrombrc]

- Added 'raiseUnauthorized' python script to plone_scripts as a
  convenience for Unauthorized exceptions to be raised from within
  page templates.
  [rafrombrc]

- Fixed #4449 by removing direct attribute access from file_view template.
  http://dev.plone.org/plone/ticket/4449
  [alecm]

- Made the navtree respect the new NonStructuralFolderInterface by
  checking is_folderish to determine if children should be shown.
  [alecm]

- Moved concatenation of actions and content to createTopLevelTabs. The
  translation of action titles is done there as well now.
  [fschulze]

- Fixed several problems in migration of ResourceRegistries.
  [fschulze]

- Made news topic sort on effective date, reversed.
  [alecm]

- Moved the news and events topics to the toplevel and removed the folders.
  If the folders had content they were renamed to old_news/events.
  [alecm]

- Made all object_buttons act on parent folder when the current object is
  the default page. Made paste target respect the NonStructuralFolder
  declaration. Made the delete alert message stronger for folders and
  default pages in folders.
  [alecm]

- Added marker interface INonStructuralFolder which allows a type to
  declare that it is a folder for implementation purposes only and should
  not be treated as such by Plone's tab generation and other is_folderish
  metadata. This is necessary to permit folderish-as-implementation types
  to not generate portal tabs at the portal root or link to folder_contents
  from a parent folder folder_contents, as well as ensure the correct
  functioning of the contents tab (displayContentsTab.py).
  [optilude]

- Fixed #4361 - OverflowError when converting to Date(Range)Indexes.
  http://dev.plone.org/plone/ticket/4361
  [stefan]

- Fixed #4366 - The envelope-from for send-to and comments is now set to the
  site admin's email ID rather than the apparent From ID entered on the form
  http://dev.plone.org/plone/ticket/4366
  [bitranch]

- Fixed #4370 - duplicate 'sharing' tab on portal root.
  http://dev.plone.org/plone/ticket/4370
  [optilude]

- Several fixes and workarounds for right to left rendering.
  [fschulze]

- Fix #4433 Changing workflow state in review_history gives KeyError:
  'comments'.
  http://dev.plone.org/plone/ticket/4433
  [hannosch]

- Fix #4456 wrong title on columns.css.
  http://dev.plone.org/plone/ticket/4456
  [hannosch]

- Added past events sub-topic events_topic/previous, and restricted the
  primary events topic to show only upcoming events.
  [alecm]

- re-added javascript_head_slot and css_head_slot to prefs_main_template,
  so that preference templates can add javascript and css like other
  templates can again.
  [elvix]

- Uncluttered the 'language' mess in the templates define.
  [deo]

   RC2 - Released August 10, 2005

- Renamed PloneTool.getOwnerId() to .getOwnerName, and made it return the
  username instead of the userid, which is importand for user sources
  where the username != userid.
  [rochael]

- Removed empty div/li in navigation tree caused by parentMetaTypesNotToQuery
  [panjunyong]

- Only show search syndication when site syndication is enabled.
  [alecm]

- Optimize the portlet_calendar again for some speed.
  [hannosch]

- Don't expand parentMetaTypesNotToQuery item in sitemap. Need more tuning.
  [panjunyong]

- Enable syndication in new plone instances and all topics by default.
  Turn off syndication tab.  Rename rss action.
  [alecm]

- Fixed #4407 by making folder_contents link to folder_contents for all
  folderish types.
  http://dev.plone.org/plone/ticket/4407
  [alecm]

- Fixed #4376 untranslated 'add type' buttons.
  http://dev.plone.org/plone/ticket/4376
  [hannosch]

- Don't clear css and javascript registries on migration from 2.0.5.
  [fschulze]

- Evaluate queryCatalog in the catalog context in getFolderContents, so
  that Smart Folders (which override queryCatalog for some silly reason)
  can still use it.
  [alecm]

- Added workaround for #4372 which is due to a strange behavior in the
  Firefox alpha. Thanks to jenner for hunting this down and contributing the
  fix.
  http://dev.plone.org/plone/ticket/4372
  [alecm]

- Addresses #2029. Now support through UI for grouping groups. UI does not
  allow a group to be added to itself or for a member (group or user) of a
  subgroup to be added to a group. Some text changed to reflect changes.
  http://dev.plone.org/plone/ticket/2029
  [gerry_kirk]

- Changed View permission restrictions on folder_constraintypes_form and
  ownership_form.  Requiring Owner restricts access to users with Owner
  role on the template itself, not the context it is called in.
  [alecm]

- Made search.pt respect typesUseViewActionInListings. Fixes part of #4373.
  http://dev.plone.org/plone/ticket/4373
  [alecm]

- Made syndication use the max_items property of the instance if set, not
  the tool.
  [alecm]

- Added ITranslatable support to getDefaultPage.
  [deo]

- Added testMissingPageIgnored to verify inexistent ids in default_page.
  Fixed a missing object in testFixFolderlistingActionNoTool.
  [deo]

- Fixed #4382 by removing unnecessary getUser call.
  http://dev.plone.org/plone/ticket/4382
  [alecm]

- Fixed #4381 by using getProperty to access listed and last_login_time
  properties in searchForMembers.
  http://dev.plone.org/plone/ticket/4381
  [alecm]

- Fixed bug triggered when reindexing order in a folder with improperly
  deleted content (i.e. when brain.getObject() returns None in
  plone_utils.reindexOnReorder(folder)).
  [alecm]

- Re-added current_page_url to global_defines for backwards compatibility.
  [alecm]

- Removed unnecessary and lazy uses of global in tal expressions.
  [alecm]

- Fixed bug: can't view a page with unauthoried related items.
  [panjunyong]

- document_relateditems are sense of typesUseViewActionInListings now.
  [panjunyong]

- Fixed bug: setting local role acquization works wrong with non-folderish
  content.
  [panjunyong]

- Removed reindex method from CatalogTool.py since it is redundant and
  as of CMF 1.5.3 differs in signature from the base type's method.
  [geoffd]

- Made language selector visible even if no document actions are defined
  for the current user
  [jok2]

- Don't require a full name for the site feedback in the contact-info page,
  as the full name is not required for members.
  [jok2]

   RC1 - Released August 1, 2005

- Added log.py module and made Plone use only one style of logging (zLOG).
  There is no logger named 'Plone' configured anywhere, so we better not
  pretend there was.
  [stefan]

- Made history table use transition titles instead of ids (requires new
  portal_workflow method).  Also localized dates in that table, and
  removed duplication of history from content_status_history.
  [alecm]

- Commented out markup code for rounded corners in the portlets. The
  tags like '<span class="portletTopLeft" />' inside the '<dl>' were
  destroying the XHTML validation because only '<dd>' and '<dt>' are
  allowed in a definition list.
  [tiran]

- Fixed issue with dashed borders in IE, and applied IEFixes which was
  going unused.
  [alecm]

- Simplified creator checking in folder_listing, as the usage of creators
  made no sense.  Let's just use Creator and be dones with it.
  [alecm]

- Making the "display" menu display the default-page if you are looking
  directly at a folder that has a default-page (e.g. its contents view)
  [optilude]

- Fixing content-type icon display in folder listing, recent portlet etc.
  [spliter]

- Fixed bottom of selected tab in IE.
  [spliter]

- Added new permission Allow Sendto to Plone. The sendto method, script
  and action are protected by the new permission. Change the permission
  in the portal root to prevent certain users like Anonymous to use or
  abuse the feature.
  [tiran]

- Fixed issue that caused Plone/AT Folders contained in a BaseBTreeFolder
  subclass to inheirt the parent index_html ComputedAttribute and attempt
  to use that as the default view resulting in a 404. Thanks to tim2p
  for finding this.
  [alecm]

- Fixed #4351 by not relying on getTypeInfo() being available on the object.
  http://dev.plone.org/plone/ticket/4351
  [optilude]

- Fixed #3906 - header now shows correct mouse pointer cursor when table is
  sortable.
  http://dev.plone.org/plone/ticket/3906
  [hannosch]

- Added migration to add new view templates to folderish types (including
  Smart Folders).
  [alecm] [limi]

- Made folder_listing and folder_contents suitable for use as Smart Folder
  views.
  [alecm]

- Fixed #2771 (#4350) using the new isURLInPortal method, which now also
  returns true on relative URLs.
  http://dev.plone.org/plone/ticket/2771
  http://dev.plone.org/plone/ticket/4350
  [alecm]

- Added default_page_types and removed non_default_page_types.  This means
  That third party-content types that want to be used as default pages
  need to be added to the list, but it also means that folderish types
  which generally don't make any sense as default pages are not allowed by
  default.  Also, made the default page selection form show the currently
  selected item.
  [alecm]

- Added CMF types to types_not_searched.
  [alecm]

- Made portlet_recent use types_not_searched to limit returned types.
  [alecm]

- Made search form use workflow state titles, and multiple columns for
  types list.
  [alecm]

- Fixed #4345 by checking the flag.
  http://dev.plone.org/plone/ticket/4345
  [alecm]

- .personal folders will no longer be created.  Fixed unit tests which
  assumed that .personal would be around.
  [alecm]

- Closed bug #4344 by limiting the number of items that can be added to the
  portal status message string when deleting items. This is really more of a
  usability fix, since we don't actually check the length of the titles; the
  full fix for the issue will appear when we merge the improved status
  message handling.
  http://dev.plone.org/plone/ticket/4344
  [optilude]

- Fixed #4346 by using the suggested fix. Thanks Tim Hicks.
  http://dev.plone.org/plone/ticket/4346
  [alecm]

- Fixed plone_javascript_variables.dtml and plone_scripts/translate.py to
  cope with i18n strings including the ' char.
  [gotcha]

- Added language to personalize form and put prefs_user_details back in
  sync with personalize.
  [alecm]

- Fixed #1490 by ensuring that sendto only works when the action is visible.
  http://dev.plone.org/plone/ticket/1490
  [alecm]

- Added an immediateLogout method to MembershipTool.py that resets the
  current security context and logs the current user out immediately.
  Used in logout.py
  [geoffd]

- Added main macros to templates which may be used as default content
  views so that they play nicely with discussion_reply_form.
  [alecm]

- Fixed #4333 prefs_user_manage now uses portal_membership.deleteMembers
  instead of acting directly on acl_users. On deletion local roles are now
  removed, but the member area is preserved.
  http://dev.plone.org/plone/ticket/4333
  [alecm]

- Added the last missing accesskey to search_form and put in a link below
  the search box.
  [hannosch]

- Re-enabled visible_ids memberdata property.  This field will determine
  the visibility of ids on a member by member basis, only if the sitewide
  property is enabled.
  [alecm]

- Fixed author home page link in author.pt
  [panjunyong]

- Change order of folderlisting/view default action determination to fix
  discussion visibility on folderish AT types.
  [alecm]

- Added javascript handler to form submit buttons which warns when the
  button gets clicked more than once.
  [fschulze]

- Fleshed out the contact-info page as a form controller page, making it
  possible to send feedback as anonymous user and as member (without
  filling e-mail address and fullname). Also displays the portal
  description.
  [jok2]

- Fixed #4335 added a method to URLTool to determine whether a URL is local
  to the portal. This will be moved into CMFCore ASAP, pending write access.
  http://dev.plone.org/plone/ticket/4335
  [alecm]

- Hooked up navtree wf config to the configlet, needs serious UI tweaking.
  Added a method to the WorkflowTool to list all wf states in the
  portal.  Added a python script that converts a list into a list of
  sublists for making columns.
  [alecm]

- Added properties wf_states_to_show, and enable_wf_state_filtering to
  navtree_properties.  These filter the navtree/sitemap/portal tabs
  results by workflow state.
  [alecm]

- Adding navigation control panel, and fixing a possible Search control
  panel migration problem in the process.
  [optilude] [limi]

- Making the livesearch result truncate title and id, as offered by jeffk
  in #4329. Thanks for the patch!
  http://dev.plone.org/plone/ticket/4329
  [optilude]

- Fixed #4324 need to ensure we are passing strings to utranslate.
  http://dev.plone.org/plone/ticket/4324
  [alecm]

- Added CMFUid tools. CMF 1.5 has a new core product CMFUid which is
  used to assign and query uids mostly like Archetypes. Products designed
  for CMF 1.5 might depend on the tools.
  [tiran]

- Fixed HEAD requests for folders. The browserDefault code mustn't look up
  the template for HEAD requests. Instead it should invoke the HEAD() api
  method defined in webdav.Collection. This fixes an ATCT bug and #4290.
  http://dev.plone.org/plone/ticket/4290
  [tiran]

- Made check_id.py prevent method aliases like 'sharing' and 'edit' as
  object ids. This fixes #4331.
  http://dev.plone.org/plone/ticket/4331
  [optilude]

- Implemented accesskeys as per accessibility-info page definition.
  [hannosch]

- Made the portal root use the /edit and /sharing method aliases for its
  'edit' and 'sharing' tabs/actions.
  [optilude]

- Made the 'view' method aliases point to '(selected layout)' instead of
  '(default view)'. This assures consistency with previous behaviour,
  so that /view at the end of a URL always gets the item itself, ignoring
  any default-page that may be set. Note that the 'view' *action* still
  points to 'string:${object_url}', so that the 'view' tab, as well as
  the '(Default)' target, still get '(dynamic view)' (and thus default
  pages) for types other than File and Image.
  [optilude]

- Fixed #4327. The live search now honours typeUseViewActionInListings.
  http://dev.plone.org/plone/ticket/4327
  [optilude]

- Fixed issue #2669. Also made the group prefs suck a bit less. These pages
  really have to be taken care of in the next release. I also disabled the
  group search feature in prefs_groups_overview because it made things much
  worse. It's no use to have a search box that doesn't search. So, now
  groups are shown using their title and descriptions for tooltips.
  folder_localrole_form also uses this info. This requires a GRUF update!!
  http://dev.plone.org/plone/ticket/2669
  [ender]

- Changed add to favorites icon in document actions to the appropriate icon.
  Before it used the site icon while the portal_type uses a heart. They must
  match and now they do.
  [ender]

- Applied patch from #4205. Better check for existence of member folders.
  Thanks to Tiran.
  http://dev.plone.org/plone/ticket/4205
  [ender]

- Made the blacklisting control in the search control panel act as a
  whitelist. That is, new types appear as selected by default and the
  backing store is a blacklist, but the user selects which type to be
  searched, not which types not to be searched, which is easier on the mind.
  [optilude]

- Created an Actions drop-down menu with cut, copy, paste and delete in
  there. I know the label is not optimal but I think this is nicer and
  cleaner.
  [ender]

- Fixed #4083. <div class="visualClear"><!-- --></div> to remove whitespace
  in IE.
  http://dev.plone.org/plone/ticket/4083
  [ender]

- Fixing #4300 by disabling the content menu when the object is in the
  factory. PLIP 24 form unload protection takes care of the other cases.
  http://dev.plone.org/plone/ticket/4300
  [optilude]

- Added link to ownership_form on the sharing page. Changed
  warning text a bit for when you visit this page for non-contentish
  items so it shows the title of the portal_type and not the id.
  The sharing page really needs to be refactored in the next release.
  [ender]

- Making prefs_group_members a form controller template, which should be
  somewhat safer from reported navigation and persistence problems, and
  makes it possible to replicate the no-search-on-page-load behaviour
  already added to prefs_users_overview. Group overview pages still not
  converted, mainly because these templates are a mess. :-(
  [optilude]

- Making the images in document_actions.pt have their height and width set
  with CSS instead of attributes on the image tag. This closes #3823, which
  advocated using the image's own height and width. This approach was deemed
  unnecessary, since we probably want them all to be consistent, and having
  to traverse to each image is an unnecessary performance hit for something
  that'll stay 16x16 almost always. :)
  http://dev.plone.org/plone/ticket/3823
  [optilude]

- Fixed #4302 using jenner's template with a few simplifications, and some
  changes to folder_contents to make reusability even easier.
  http://dev.plone.org/plone/ticket/4302
  [alecm]

- Finished #1805 without any catalog metadata even. Added a method to
  WorkflowTool that retrieves a state title given a state id and a
  portal_type. As a result it can be used for brains and objects alike.
  http://dev.plone.org/plone/ticket/1805
  [alecm]

- Making member overview preference page not perform a full member search
  by default, but adding a "Find all" button to find all members if you
  need this listing. This fixes #2530. The bug also mentions that we could
  have "Find all" the default behaviour when there are sufficiently few
  members. However, there has been no followup on how we can efficiently
  count the number of members, so this is still an open feature request.
  http://dev.plone.org/plone/ticket/2530
  [optilude]

- Adding display of currently selected default-page to "display" menu and
  cleaning up markup a bit. Still some CSS work to be done before this is
  fully OK.
  [optilude]

- All icons for content types are now displayed using CSS - closes #3138.
  http://dev.plone.org/plone/ticket/3138

- Removed all references to getStateClassName() as this was just a
  makeshift solution that was used before we got the normalizeString()
  method in PloneTool.
  [limi]

- Hooked up the new HTML-formatted and improved start page
  [limi]

- Reverted change to normalizeString as Archetypes relied on it in the
  title to id autogeneration code.
  [hannosch]

- Fixed #3242 added And/Or search option to Subject field on search_form.
  http://dev.plone.org/plone/ticket/3242
  [alecm]

- Fixed #3211 by updating the permission on PloneTool.setMemberProperties,
  the other permissions are fixed in CMF 1.5.
  http://dev.plone.org/plone/ticket/3211
  [alecm]

- Fixed #4242 by updating test.
  http://dev.plone.org/plone/ticket/4242
  [alecm]

- Fixed inappropriate condition on folder_constraintypes_form.
  [alecm]

- Made tableless skin use showEditableBorder, fixed #4291.
  http://dev.plone.org/plone/ticket/4291
  [alecm]

- Fixed failing unit tests due to cleanupFilename removal. atct's base.py
  _setATCTFileContent method relied on getting a false value back from
  normalizeString when called with None.
  [hannosch]

- Removed text size actions, moved Site Setup action to site_actions, and
  added contact and accessibility site_actions.
  [alecm]

- Added in some more character mappings to UnicodeNormalizer that were
  defined in ATCT's now removed cleanupFilename method
  [hannosch]

- Remove accesskeys as they are interfering with screen reader shortcuts.
  This fixes #3535.
  http://dev.plone.org/plone/ticket/3535
  [hannosch]

- Migrated to some nicer workflow state titles.
  [alecm]

- Fixed issues related to External Editor action (2939, 3008, 4176), using
  a script from glenfant.  The icon appears only when both 'Modify portal
  contents' and 'Use external editor' are available, the user has the a
  member property set, and the object supports WebDAV editing/locking, and
  isn't locked.
  http://dev.plone.org/plone/ticket/2939
  http://dev.plone.org/plone/ticket/3008
  http://dev.plone.org/plone/ticket/4176
  [alecm]

- Partial fix for #4272 some missing i18n markup.
  http://dev.plone.org/plone/ticket/4272
  [hannosch]

- Added 'Large Plone Folder' to parentMetaTypesNotToQuey navtree_property.
  This ensures that large folders will not display their contents in the
  navtree.
  [alecm]

- Fixed #4251. ulocalized_time() fetches all DateTime errors and logs them.
  http://dev.plone.org/plone/ticket/4251
  [tiran]

- Took care of #4224 by disabling the ZMI ordering interface for the
  Plone Site object.
  http://dev.plone.org/plone/ticket/4224
  [stefan]

- Removed PropertyManagedBrowserDefault, and update the portal root support
  BrowserDefaultMixin as implemented by CMFDynamicViewFTI.
  [alecm]

- Fixed #4216 - migration would add 'contents' action more than once.
  http://dev.plone.org/plone/ticket/4216
  [stefan]

- Changed category of 'view' and 'edit' actions on 'Plone Site' to
  'object'.
  [alecm]

- Implemented limi's suggestion for contents tab.
  [alecm]

- Fixed discussion_reply_form to work with CMFDynamicViewFTI stuff.
  [alecm]

- Added dummy savepoint method to transaction\_.py
  [tiran]

- Resurrection of old edit template for CMF content types. It is possible
  to edit and view old style content types again. These templates should be
  removed in 2.5.
  [tiran]

- Added pretty_title_or_id method to PloneTool which returns the Title
  or non-autogenerated id, otherwise it returns a translatable default
  string (or a given default parameter).  Made plone use this method
  (or the helper python script that points to it) everywhere.  Currently
  this incurrs a skin lookup and script call for nearly every content item
  listed (portlets, listings, etc.). This method could easily be added to
  catalog metadata if the penalty is too large, with no need to change the
  templates.  However, doing so would loose the translatability of the
  default string.  Something like 'context/pretty_title_or_id|empty_title'
  won't work as '|' only triggers on an exception, so a python expression
  would be needed to maintain translatability.
  [alecm]

- Added isIDAutogenerated method to PloneTool and deprecated the python
  script. This method is normally used from FS code and so it belongs in
  FS code.
  [alecm]

   Beta1 - Released July 7, 2005

- PloneFolderBase (and hence LargePloneFolder) no longer inherits
  SkinnedFolder, as SkinnedFolder has OrderSupport in CMF 1.5.
  [alecm]

- Moved reindexOnReorder stuff into PloneTool, and use it from the
  folder_position script.  This way non-ATCT/PloneFolder types get proper
  reordering in the GUI.  Order reindex on rename is still not available
  for custom types.
  [alecm]

- Added the phrase "Open Source" to the colophon to keep google happy
  [geoffd]

- Fixed #4263 - method alias handling in portal_factory.
  http://dev.plone.org/plone/ticket/4263
  [geoffd]

- Fixed #4258 - Added support for parentMetaTypesNotToQuery to the navtree.
  http://dev.plone.org/plone/ticket/4258
  [alecm]

- Use the old fashioned (but badly named) metaTypesNotToList for the
  navtree blacklist, instead of reinventing the wheel, appending the
  necessary new values to that list in migration.
  [alecm]

- Use a global define for visible_ids so that it is automatically used for
  custom types.
  [alecm]

- Ceiling date patch is obsolete for CMF 1.5 - removed it.
  [hannosch]

- Fixed #4247 - remove unused group_submit variable.
  http://dev.plone.org/plone/ticket/4247
  [hannosch]

- Made it possible to show action icons in personal-bar.
  [fschulze]

- Fixed #4229 - Error in sharing tab, roles.append changes a list inplace.
  http://dev.plone.org/plone/ticket/4229
  [hannosch]

- Fixed #4241 - MembershipTool.py used _checkPermission without importing it
  http://dev.plone.org/plone/ticket/4241
  [hannosch]

- Added is_default_page index to catalog, and made navtree no longer show
  objects which are the default page in a folder.
  [alecm]

- Fixed a number of security related issues.  We cannot assume that we can
  access attributes of the parent object (this includes using 'folder' in
  actions and 'aq_parent' in skins).  This fixes viewing visible objects
  in private folders, and also some PLIP 16 issues.
  [alecm]

- Made NavTree use a black list of portal_types not a white list.
  [alecm]

- Removed data/navigation_properties that was deprecated in Plone 2.0, as
  well as the data/ directory. Migrations to remove the property sheet
  from ZODB has been added before.
  [vinsci]

- Refactoring use of __browser_default__() to use CMF 1.5-style aliases
  and FTIs, with __browser_default__() still being the fallback for old
  classes. Some tests had to be fixed for this, too.

  Adding aliases for view, edit, properties, sharing. Fixing up some uses
  of getActionById() which were failing because of these aliases.

  Note that we now depend on fixes to CMFFormController, ATContentTypes and
  CMFDynamicViewFTI checked in alongside this commit.
  [optilude]

- CMF 1.5 Cookie Crumbler distinguishes between login attempt and
  authorization failure, making require_login obsolete.
  [stefan]

- Added a configlet for setting search options, to enable/disable LiveSearch
  and to set the types_not_searched property. This is requested in #4032.
  http://dev.plone.org/plone/ticket/4032
  [jok2]

- Moved some interfaces to CMFDynamicViewFTI
  [tiran]

- Changed unload protection, so only forms with
  class="enableUnloadProtection" are checked.
  [fschulze]

- Slight change to navigationParent script so that it won't fail
  when a Z3 view is in the acquisition tree
  [rafrombrc]

- Added recently_modified page to link to from the recent changes
  portlet.
  [ender]

- Added state coloring in recent changes portlet and search results.
  [ender]

- Total rewrite of portlet HTML and CSS. Will keep backwards compatibility
  until Plone 2.5 is released, though. The old div-based layout is
  deprecated in favor of a more light-weight markup using definition lists
  and allowing interesting skinning variations - round corners using CSS,
  for example. It also has bigger click areas, making it easier to navigate
  the portlets.
  [limi]

- Changed dropdowns slightly, now the activated/deactivated class is set
  on the dl, not on the dd. When javascript is disabled, the dropdowns
  don't have an arrow anymore.
  [fschulze]

- Simplified collapsibles, this involves new markup. This fixes #4035 -
  "Collapsible fieldsets take up too much space".
  http://dev.plone.org/plone/ticket/4035
  [fschulze]

- Fixed PloneFolder.manage_delObjects() so it returns to the ZMI.
  Thanks to George Geller.
  [stefan]

- Moved some interfaces to CMFDynamicViewFTI
  [tiran]

- Removed plone prefix from stylesheets, only ploneCustom.css is kept.
  [fschulze]

- Refactored the dropdown menu. It's using css classes for styling of
  visibility. This involves new markup for the menus.
  Fixes #2793 - ADD ITEM MENU cuts some entries.
  http://dev.plone.org/plone/ticket/2793
  [fschulze]

- Tiny change to the nav tree code in PloneTool.py so the nav tree won't
  barf when there is a Z3-style view class in the acquisition hierarchy
  [rafrombrc]

- Some i18n markup corrections after loginageddon and one metadata file
  in the wrong place, fixed #4197.
  http://dev.plone.org/plone/ticket/4197
  [hannosch]

- Loginageddon!  Moved login, logout, and registration-related forms
  and scripts to the new plone_login skin.  Converted login forms and
  scripts to formcontroller forms and scripts.  Moved cookie testing
  and related javascript from login_form into login.js.  Made the
  cookie test messages internationalizable.  Made login sequence fail
  more gracefully when cookies are disabled.  Added nice error
  messages that explain why a login failed (e.g. no login name, no
  password, and (optionally) login name not found).  The login name
  not found test can be enabled/disabled via a new site_property,
  verify_login_name. Fixes 2408, 2458, 2250, and 3335.
  http://dev.plone.org/plone/ticket/2250
  http://dev.plone.org/plone/ticket/2408
  http://dev.plone.org/plone/ticket/2458
  http://dev.plone.org/plone/ticket/3335
  [geoffd]

- Fixed #3018 - no duplicate id="portal-footer".
  http://dev.plone.org/plone/ticket/3018
  [hannosch]

- Added filtering of tests to ECMAScript Unit Tests.
  [fschulze]

- Add cssQuery.js to portal_javascripts when installing or migrating.
  [fschulze]

- Moved 3rd party ecma scripts like sarissa, livesearch, ecmaunit and
  vcXMLRPC to plone_3rdParty. 3rd party code will be included by an
  svn:external rule soon.
  [tiran]

- Reactivated alternate font size stylesheets.
  [fschulze]

- Added some missing i18n markup. Fixed ZChecker error regarding '>'
  [hannosch]

- Fixed migrations of older instances caused by the ResourceRegistries
  refactoring. If you updated and migrated while this was still broken,
  then you might have to force a migration from alpha2 or even alpha1.
  [fschulze]

- Added framework for ECMAScript Unit Tests.
  [fschulze]

- Partially fixed #4077 and #3535 accesskeys are properly defined now, but
  still need to be changed to numeric values.
  http://dev.plone.org/plone/ticket/3535
  http://dev.plone.org/plone/ticket/4077
  [hannosch]

- Fixed #2414 all literal msgid's converted to non-literal.
  http://dev.plone.org/plone/ticket/2414
  [hannosch]

- Merged plip83-kupu-integration r7083:7084 into 2.1 branch.
  [stefan]

- Fixed #1382 - Redirection after login has been changed. Original behavior
  is to strip any query string passed before redirecting. Now, if query
  string exists (such as when coming from discussion_reply_form.pt), don't
  strip it off.
  http://dev.plone.org/plone/ticket/1382
  [briang]

- Fixed #2756 - portlet_calendar localization is working now. had to
  introduce a new method on the calendar_tool to get the correct daynumbers.
  http://dev.plone.org/plone/ticket/2756
  [hannosch]

- Fixed #3365 calendar_slot.pt has been moved to
  plone_templates/calendar_macros.pt and cleaned up.
  http://dev.plone.org/plone/ticket/3365
  [hannosch]

- Fixed #4136 - you couldn't pick january or the first of a month with the
  js date picker, reflected changes in the tests.
  http://dev.plone.org/plone/ticket/4136
  [hannosch]

- Fixed #3256 - Plone Config -> Add/Remove Products: Added
  "product filesystem version" in the message displayed for products that
  need updating.
  http://dev.plone.org/plone/ticket/3256
  [briang]

- Fixed #4164 the getIcon and getTypeInfo calls were no longer needed.
  http://dev.plone.org/plone/ticket/4164
  [alecm]

- Fixed #4055 by returning an empty list in getAddableTypesInMenu if the
  View permission is not available.
  http://dev.plone.org/plone/ticket/4055
  [alecm]

- Fixed #4114 by adding new criteria to the news and events topics.
  http://dev.plone.org/plone/ticket/4114
  [alecm]

- Fixed #4149 - incorrect tal:define for locked items in the byline.
  Thanks to Raphael Ritz for the fix.
  http://dev.plone.org/plone/ticket/4149
  [optilude]

- Removed review_state='published' from the query for author page and
  navigationLocalRelated. Catalog deals with permissions already.
  http://dev.plone.org/plone/ticket/2304
  [ender]

- Fixed #3714. Use ACTUAL_URL to skip to content.
  http://dev.plone.org/plone/ticket/3714
  [ender] [neaj]

- Fixed #4137 by introducing a keyword argument 'show_inactive'to
  CatalogTool.searchResults and queryCatalog which disables expiry
  filtering.  Also granted the 'Access inactive portal contents' permission
  to Owner in migration, and made getFolderContents to pass the
  'show_inactive' parameter when the current user has that permission on the
  relevant folder.
  http://dev.plone.org/plone/ticket/4137
  [alecm]

- Introduced a Zope 2.8-style transaction module. Plone code should now use
  'from Products.CMFPlone import transaction' which will work in Zope 2.7
  and Zope 2.8.
  [stefan]

- Moved transaction_note, base_hasattr, safe_hasattr, and safe_callable
  to the utils module. Got rid of AT-style shasattr. Fixed safe_callable
  and made sure we use our version of safe_callable throughout.
  [stefan]

- Fixed #3410 by declaring enumConfliglets public. The method does its own
  security checks for each configlet action.
  http://dev.plone.org/plone/ticket/3410
  [alecm]

- Fixed index_html hack to return 404 for requests other than
  (PUT, HEAD, GET, POST).
  [sidnei]

- Updated "my folder" action to point straight to folder, not to
  folder_contents
  [optilude]

- Changed 'batch' action which was previously hidden by a condition in
  global_contentmenus to use a pair of actions, batch and nobatch, with
  mutually exclusive conditions. This effectively creates a toggle, which
  is much more sensible than having to click the 'view' tab to get back.
  [optilude]

- Fixed #3688 and added a test. Also added a test to ensure that
  portal_factory respects PLIP 16 local role inheritance.
  http://dev.plone.org/plone/ticket/3688
  [geoffd]

- Fixing markup to make zchecker happy and changed table summaries to use
  non-literal msgids, plus some minor i18n changes.
  [hannosch]

- Fixing #4106 - arrow is in wrong direction in breadcrumbs when using RTL
  sites. When using mixed RTL and LTR content, the order is jumbled, though
  - not sure if this is common in those languages.
  http://dev.plone.org/plone/ticket/4106
  [limi]

- Fixed #4089 - fix some i18n markup.
  http://dev.plone.org/plone/ticket/4089
  [hannosch]

- Fixed #2659 - using patch by fschulze.
  http://dev.plone.org/plone/ticket/2659
  [alecm]

- Fixed #4049 - the template showing the discussion threads at the bottom of
  an item's view template now has a more sensible check to make sure it
  picks the correct view template.
  http://dev.plone.org/plone/ticket/4049
  [optilude]

- Fixed #3279 integrate new jscalendar 1.0.
  http://dev.plone.org/plone/ticket/3279
  [hannosch]

- Overrode listTypeInfo from CMFCore.TypesTool.  The original method was
  doing security checks on the TypeInformation objects themselves in
  addition to the isConstructionAllowed test.  This was very expensive and
  only useful if someone had set custom security restrictions on some
  TypeInformation objects in the types tool through the ZMI.  I cannot see
  a reasonable reason for someone to do such a thing.  Also, removed a
  check for null TypeInfo.getId(), as this will never happen, if it
  does it's a bug in and of itself and shouldn't be ignored.  Also,
  changed the check shich ensures that our objectValues() are TypeInfoish
  to use the clear and sane interface.isImplementedBy(obj) instead of the
  getattr(aq_base(type),'_isTypeInformation',0) it was using before.
  [alecm]

- Fix browserDefault() in PloneTool so that images and files work, and there
  are less wtf moments. Look at

  http://plone.org/documentation/manual/plone-developer-reference/
    specific-areas/content-types/zope-to-browser

  for details on how the implementation works.

- Make object paste button act on parent folder for folderish default
  pages.
  [alecm]

- Fixed folder_contents listing table in RTL stylesheet (#4155).
  http://dev.plone.org/plone/ticket/4155
  [andrewb]

   Alpha2 - Released May 25, 2005

- Fixed the way newsitem_view.pt tests for the (optional) image thumbnail.
  [tiran]

- Disabled HTTP compression for .css and .js files by default. You can turn
  it on by editing skins/plone_scripts/enableHTTPCompression.py.
  [stefan]

- urlquote the external_edit path to make exteranl editor work with
  Chinese id better
  [panjunyong]

- Fixed some syndication breakages, and added unit tests for
  portal_syndication.
  [alecm]

- Fixed #4081 changed 'Plone Setup' to 'Site Setup'.
  http://dev.plone.org/plone/ticket/4081
  [limi] [alecm]

- Fixed #2850 added on-error handler to portlet_fetcher, currently provides
  no traceback as tracebacks are not accessible from untrusted code.
  http://dev.plone.org/plone/ticket/2850
  [alecm]

- Fixed #2586 changed MembershipTool.getCandidateLocalRoles() to use
  member.getRolesInContext(obj) instead of member.getRoles(), and to use
  obj.valid_roles() instead of MembershipTool.getPortalRoles(). This
  allows loal managers to assign any role, and allows all managers to
  assign roles that exist only locally and not at the plone root. A side-
  effect is that roles defined in the zope root and other folders beneath
  the portal root will be available as well, just as they are in the ZMI.
  http://dev.plone.org/plone/ticket/2586
  [alecm]

- Merged PLIP 98 - Scripted Translation Service Interface. This adds a
  'translation_service' tool to Plone which replaces the not-quite-sane
  methods in CMFPlone.utils. UnicodeDecodeErrors should now crop up significantly
  less often.
  [longsleep] [stefan]

- Fixed #3267 removed invalid transition validity test using the fix by
  blueszhao in the issue.
  http://dev.plone.org/plone/ticket/3267
  [alecm]

- Applied #4052 titleToNormalizedId (normalizeString) improvement. Object
  id from title generation should now work with most accented characters.
  It is possible to define custom normalizations in UnicodeNormalizer.py.
  http://dev.plone.org/plone/ticket/4052
  [naro]

- Added styles that make the editing widgets look more like their view
  counterparts.
  [limi]

- Make portlet_favorites work again and use the catalog like everything
  else. Also, use the addable types restrictions in users' Favorites
  folders.
  [alecm]

- Fixed an obvious issue at global_defines when there's no portal_tabs
  actions.
  [deo]

- Made external editing a user preference. It defaults to the setting in the
  memberdata tool. Migrations should work as well.
  [ender]

- Showed icon in byline to change ownership.
  [ender]

- Added jscript that hides traditional add items pull-down in
  folder_contents.
  [ender]

- Major refactoring of the CSS, removed all the old navtree classes,
  made most of the templates use the new auto-generated `contenttype-*`
  classes, and lots of other CSS fixes and tweaks.
  [limi]

- Disabled 'Add to favorites' action until favorites are refactored
  in future plone versions.
  [ender]

- Modified labels in personal bar. Removed 'my this' and 'my that'.
  It's already a personal bar.
  [ender]

- Renamed titleToNormalizedId to the variation preferred by limi
  normalizeString()
  [alecm]

- Fixed #4062 - made history_form show true causes for an empty page, rather
  than always assuming that the error is due to missing Historical interface
  http://dev.plone.org/plone/ticket/4062
  [alecm]

- Added automatically generated classes for content types. You can now
  always get a class "contenttype-news-item" for every content type
  installed. It is normalized according to the same rules as IDs.
  [limi]

- Replaced registered_notify_template and mail_password_template
  DTMLs with page templates. See #3483.
  http://dev.plone.org/plone/ticket/3483
  [dpunktnpunkt]

- More spring cleaning: Removed the implicit removal of underlining links -
  Plone now specifies explicitly when it wants the link to not have an
  underline, and defaults to having it, like the good HTML citizen it is.
  Some products may get underlines on links that didn't have them before,
  but this should be trivial to fix, and is worth it in the long run.
  [limi]

- Finally removed all implicit margins from Plone's input elements - if
  this leads to some slight disturbances in the force (ie. some of your
  form elements have explicit margins added to compensate for the old
  behaviour), I apologize - but this has been around since Plone 1.0, and
  is just very confusing when you use the form elements. Should be easy
  to adjust in your Product - just remove the margins you added to the
  input tags.
  [limi]

- The tag rendering the description attribute is left out if there's no
  description, it also uses a paragraph tag instead of a div now.
  Resolves #3841.
  http://dev.plone.org/plone/ticket/3841
  [limi]

- Added icons for feed:// and webcal:// links.
  [limi] [elvix]

- Fixed #2844 - made WorkflowTool.getTransitionsFor return the action_url.
  This is not currently used for the content menu, but it does allow
  developers to access this information for tighter control over transitions
  for custom workflows. Added new testWorkflowToool.py with one lonely test.
  http://dev.plone.org/plone/ticket/2844
  [alecm]

- Fixed #2867 put the list reversal in content_status_history in the proper
  place.
  http://dev.plone.org/plone/ticket/2867
  [alecm]

- Fixed #2416 by updating document_byline to use the portal script. Changed
  the isExpired script to prefer the DC Metadata accessor 'ExpirationDate',
  but fall back on 'expires'. Also, it now uses safe_callable to determine
  whether we have an accessor or catalog metadata, rather than strange
  looking exception handling.
  http://dev.plone.org/plone/ticket/2416
  [alecm]

- Changed the bogus 'ExipresDate' metadata from CMFCore to the DC
  'ExpirationDate' during migration.
  [alecm]

- Added safe_callable method to __init__.py.  This is acquisition and
  ConfilctError safe (it uses shasattr), and should be used in place of
  callable() when possible.
  [alecm]

- Add 'shasattr' from Archetypes.utils to __init__.py, make the existing
  'base_hasattr' a wrapper around this safer more flexible method.
  Please use this in python scripts and elsewhere in place of 'hasattr'
  which has serious potential issues.  Can be imported with
  'from Products.CMFPlone import shasattr'.
  [alecm]

- Fix livesearch_reply and queryCatalog so that they quote parentheses.
  Otherwise a parse error is thrown. Fixes #3067 the other listed characters
  from the Silva bug report don't appear to cause problems.  Also, apply
  quote_logic if enabled to Title and Description text searches, not just
  SearchableText by default.
  http://dev.plone.org/plone/ticket/3067
  [alecm]

- Made the livesearch_reply query a little less strange.  It used to turn
  'my dumb query' into 'my* and dumb* and query*' which is strange, now it
  just does 'my AND dumb AND query*'.  Also, the more link was just doing
  'my+dumb+query', which results in an entirely different set of results
  than shown in the dropdown, now it uses the same query as the dropdown.
  [alecm]

- Use plone_utils.getUserFriendlyTypes() to do type restriction on
  LiveSearch just like everywhere else.
  [alecm]

- Remove permission check in search_form, there's no reason to disallow
  review_state searches to users that are not granted 'Review portal
  contents' on the portal root.  The catalog enforces 'View' security
  just fine. Resolves #2175.
  http://dev.plone.org/plone/ticket/2175
  [alecm]

- PloneTool._makeTransactionNote() now uses the site encoding not UTF-8.
  [alecm]

- Made folder_cut, folder_copy, folder_paste, and folder_position redirect
  to the originating template not hardcoded folder_contents.
  [alecm]

- Fixed #850: Allow discussions to be closed.  I changed
  viewThreadsAtBottom to list existing discussion items even if
  discussion is disabled.  This requires our own
  portal_discussion.getDiscussionFor, because CMFDefault's raises
  DiscussionNotAllowed on this get operation.

  I also added a check for
  portal_discussion.isDiscussionAllowedFor in validate_talkback
  because, funnily enough, DiscussionNotAllowed isn't raised on
  createReply in DiscussionItem when it's turned off.
  http://dev.plone.org/plone/ticket/850
  [dpunktnpunkt]

- Added a getGroupInfo() public method to the portal_groups tool, like
  getMemberInfo() in portal_membership tool.
  [gerry_kirk]

- Made the navTree breadcrumbs and folder based portal tabs use the new,
  typesUseViewActionInListings property to determine the appropriate url.
  Also, added some extra unit tests for the above PloneTool methods.
  This and the previous entry should resolve issues #928 and #2373.
  http://dev.plone.org/plone/ticket/928
  http://dev.plone.org/plone/ticket/2373
  [alecm]

- Added a new typesUseViewActionInListings property in site_properties
  which can be used for types whose immediate view is not desirable to
  link to from folder_contents or folder_listing (currently Image and
  File). Also, typesLinkToFolderContentsInFC is no longer used, and
  listing templates have been simplified a bit.
  [alecm]

- Gave a title to the Favorites folder.
  [alecm]

- Refactored the way portal discussions are displayed. They are now shown
  in an expanded way so no more clicking is needed to read the entire
  discussion.
  [ender]

- Added methods for retrieving version tuples to utils module (FS
  version only) and to MigrationTool (both FS and instance versions)
  [rafrombrc]

- Added charset to the Content-type header when use RSS to fixed some
  encoding problem.
  [panjunyong]

- Added [duncanb]'s update for bug #3294. Tables no longer need an id
  attribute to be sorted.
  http://dev.plone.org/plone/ticket/3294
  [elvix]

- Added fix for bug #4027. feed:// and webcal:// links now get special
  css-classes so that they may be styled appropriately.
  http://dev.plone.org/plone/ticket/4027
  [elvix]

- Changed the 2.1 migrations so that they make sure the MemberDataTool is
  the default (i.e. not CMFMember) before trying to manipulate the
  properties on the tool, since a) modifying the properties on CMFMember's
  MemberDataContainer doesn't accomplish anything and b) property
  name conflicts were causing the Plone migrations to fail in sites
  w/ CMFMember installed
  [rafrombrc]

- Changed the global_defines attribute 'isFolder' to 'isFolderish' - it
  was only used in one location in the Collective projects I checked, and
  one location in Plone itself - and didn't really test the right thing.
  It was also expensive. If you have a third-party product that was using
  'isFolder' for anything, you should update your code.
  Removed redundant check in content_status_history as a result.
  [limi]

- Updated 'ownership_form' to not display the subobjects checkbox if the
  item is not folderish.
  [limi]

- Added rel="nofollow" attribute to calendar links. Should ultimately
  be restricted by a year range, but this is a quick workaround.
  Closes http://plone.org/development/teams/ui/tasks/89
  [limi]

- Added support for searching for members who have NOT logged in
  since the specified last_login_time.
  [rafrombrc]

- Added Description, Location, Language and Home Page to Author page.
  [limi]

- Fixed permissions and conditions on folder 'cut' and 'copy' actions
  previously they used 'View management screens' and 'Modify portal
  contents'. Removed action creation from setup/ConfigurationMethods.py for
  these and change_state.
  [alecm]

- Fixed #2836 - Review portal contents or Modify portal contents is
  sufficient to show the change_state action.
  http://dev.plone.org/plone/ticket/2836
  [alecm]

- Changed member_search_form.pt so that it submits last_login_time as
  a plain DateTime object rather than a catalog style query dictionary.
  [rafrombrc]

- Exposing 'language', 'home_page', 'location' and 'description' in
  getMemberInfo() in the MembershipTool. These are used in author.pt.
  [limi]

- Added ploneGenerated.css for programmatically generated classes, and
  ploneMember.css for logged in users (for state coloring etc).
  Cleaned up the configuration a bit (added media declarations), updated
  tests.
  [limi]

- Changed 'news' and 'Members' portal tabs migration so that it disables,
  rather than deletes the actions.  No need to be destructive.
  [alecm]

- Added new portal_memberdata properties 'home_page', 'language',
  'location', 'description' (text) at limi's request.
  [alecm]

- Fixed #3095 - You can now use actions to create tabs for folders not at
  the portal root and the tab highlighting will work correctly. This is done
  by comparing the current object path to the actions url (i.e. the id of
  the action no longer has to be related to the resulting url).
  http://dev.plone.org/plone/ticket/3095
  [alecm]

- Fixed #3681 - No longer allow to add content with ids of skin scripts.
  http://dev.plone.org/plone/ticket/3681
  [whit537]

- Fixed #3999 - check_id now gives better error messages.
  http://dev.plone.org/plone/ticket/3999
  [whit537]

- Fixed #1987 - 'batch' mode now enabled whenever the List folder contents
  property is available and one or more of the modification permissions is
  available (Delete, Copy, Add, Modify). These checks apply to the current
  object if it is folderish and not set as the Default Page for its parent;
  otherwise, the checks are made on the parent.
  http://dev.plone.org/plone/ticket/1987
  [alecm]

- Fixed #2912 - "Format" renamed to "MIME type" in metadata form to avoid
  confusion with the text format selector.
  http://dev.plone.org/plone/ticket/2912
  [limi]

- Fixed #3938 - duplicate class definitions for .even and .odd.
  http://dev.plone.org/plone/ticket/3938
  [limi]

- Manually merged Duncan's plip24-form-unload-branch.
  Plone will now present a warning message if the user tries to navigate
  away from a page with a changed form.
  [duncanb][elvix]

- Changed encoding to utf-8 on javascript files to stay in sync with the
  rest of Plone.
  [elvix]

- Enabled the "display" menu on the portal root. You can set the templates
  to be available there using the property "selectable_views" at the root
  portal object. Also renamed the front page from index_html to front-page
  and set is as the default page during portal creation, in order to make
  the "display" menu work as expected immediately after portal creation.
  [optilude]

- Made sure PloneTool.changeOwnershipOf() works recursively.
  [stefan]

- Fixed user and group name/id fuzzyness in PloneTool.changeOwnershipOf()
  and folder_localrole_form.pt.
  [stefan]

- Reworked prefs_users_overview to use CMFForumController and to
  simplify prefs_user_manage.cpy.
  [bmh]

- Fixed #3931 - add 'more ...' link to events portlet, also added new events
  tab/folder and topic to match the news folder/tab and topic.
  http://dev.plone.org/plone/ticket/3931
  [lucas]

- Fixed #3752 - return rss search results in effective date order
  (reversed), unless another order is explicitly given.
  http://dev.plone.org/plone/ticket/3752
  [alecm]

- Changed portlet_news.pt and news_listing.pt to do the right
  thing if the 'news' folder at the root of the site isn't
  there.
  [rafrombrc]

- Added some argument type sanity checking to queryCatalog.py;
  it was failing on valid queries b/c it was making assumptions
  about the types that it was receiving.
  [rafrombrc]

- Add charset info for ZMI pages like addSite.zpt and addPropertySheet.zpt
  for better Chinese support.
  [panjunyong]

- Fixed #3901 - applied the PloneTool.py patch by F Bennett (bierce), which
  shows full listing of inherited roles.
  http://dev.plone.org/plone/ticket/3901
  [alecm]

- Fixed #3819/ - applied the utils.py patch provided by gkirk.
  http://dev.plone.org/plone/ticket/3819
  [rafrombrc]

- Fixed prefs_user_details to only display user roles and not
  roles inherited via groups since those can't be edited on this
  form.
  [bmh]

- Fixed #3848/ - changed prefs_error_log_update.py to match the button
  submit values on prefs_error_log_form.
  http://dev.plone.org/plone/ticket/3848
  [rafrombrc]

- Minimally reworked user/group control panel pages to plone2.X
  style fixing #2204 and possibly others.
  http://dev.plone.org/plone/ticket/2204
  [bmh]

- Updated all references to CSSRegistry to the new, renamed,
  ResourceRegistries. Migrations, tests. Instead of name-confusion, there is
  now the product ResourceRegistries containing the two tools CSSRegistry
  and JSregistry.
  [elvix]

- Fixed #3835 - Changed .metadata file of prefs_user_manage.cpy script to
  redirect instead of traverse on success.
  http://dev.plone.org/plone/ticket/3835
  [gkirk]

- Fixed #3903 - Removed hardcoded references to logo.jpg in favor of the
  logoName variable defined in base_properties.
  http://dev.plone.org/plone/ticket/3903
  [bmh]

- Fixed #3544 - Use password_confirm as the name of the password
  confirmation field so it doesn't show up in error logs.
  http://dev.plone.org/plone/ticket/3544
  [bmh]

- Fixed #3811 - Start and end times of same-day events now respect AM/PM
  settings (event_view).
  http://dev.plone.org/plone/ticket/3811
  [naro]

- Made folder actions (cut, copy, rename, delete, publish) give nice
  message instead of error when the selected item is no longer available.
  Fixes issue #3911.
  http://dev.plone.org/plone/ticket/3911
  [alecm]

- Made sortable_title use the site-encoding to store the final value (not
  direct unicode). Also, made sortObjects.py case insensitive.
  [alecm]

- Fixed #3866 - Improved performance of sortObjects helper script by a
  factor of 3.
  http://dev.plone.org/plone/ticket/3866
  [axa]

- Fixed #2791 - Timestamps in recently_published and folder_contents now use
  the configured long format.
  http://dev.plone.org/plone/ticket/2791
  [naro]

- Add a hook to call a method or script 'getCustomNavQuery' to createNavTree
  and createTopLevelTabs.  This method should return a dict to augment the
  catalog query (i.e. require specific workflow state or custom property),
  the parameters will not override any of the default parameters.
  [alecm]

- Add a disable_folder_sections to site_properties so that people who don't
  want to use top-level folders for tabs can just use the actions in the
  original manner.
  [alecm]

- Made the default news folder view a Topic at limi's request.  Made
  changes to the way folderish default documents are handled to make the
  UI for this sensible.  Folderish default pages now act entirely
  non-folderish as far as global_contentmenu is concerned.  If such an object
  wants to have a batch view, add buttons, view control, etc. it must
  implement them as object actions (like the sub-topic form).  Also, fixed
  a bug which caused folderish types that had no preset template views
  to not show their selectable default view menu, leaving a non-working
  display menu.
  [alecm]

- Add support for the 'pghandler' argument added in Zope 2.8
  (though we don't officially support Zope 2.8 yet).
  [sidnei]

- Changed the order of the documentActions in the default view templates.
  If you have customized your view templates, you need to move these
  above the headline tag. Sorry about the inconvenience, but the existing
  positioning was triggering too many browser bugs. This keeps it simple.
  Look at 'document_view' if you need an example.
  [limi]

- Publishing the default document in a folder now publishes the folder as
  well, if possible (and similarly, making the default page visible or
  private will make the folder visible or private as well)
  [optilude]

- content_status_history (Change state button from folder_contents or
  'advanced' item in state drop-down) is now more consistent, showing
  the items being affected in both cases, and permits the publishing of
  folder contents along with a folder no matter which method is used.
  [optilude]

- Default content types are now in portal_factory
  [optilude]

- registered_notify_template now honours the 'email' parameter passed in
  instead of using 'member.email', and in the process no longer breaks
  CMFMember
  [optilude]

- Merged (some variation of) madduck's member area type selection branch.
  This allows to configure the portal type used for home folders in the
  membership tool.
  [stefan] [madduck]

- Fixed non-ASCII character issue in sortable_title method.
  [alecm]

- Fixed up permissions on new cut/copy/delete actions.
  [bmh]

- Fixed #3384 by catching CopyError so users don't get dumped into the ZMI.
  http://dev.plone.org/plone/ticket/3384
  [bmh]

- Made sortable_title do useful numerical sorting, and truncate values
  longer than 30 chars to prevent bloat.
  [alecm]

- is_folderish metadata added. It contains bool(isPrincipiaFolderish)
  [tiran]

- sortable_title FieldIndex added by popular demand.
  [alecm]

- Made folder_contents useful for viewing and altering non-local content
  (try folder_contents?path=/).  Changed folder_delete, folder_publish,
  and folder_rename to work with paths instead of ids (and altered
  corresponding forms).  Added new method to workflow tool to get workflow
  transitions for objects given by path rather than id.  Made the
  aforementioned scripts redrect to the originating form instead of
  hard-coded folder_contents (uses request variable 'orig_template').
  Removed copy, cut, paste buttons when the folder_contents view isn't
  local, as those actions won't work properly in that circumstance (copy
  can probably be implemented, but will need to use some OFS internals).
  Added tests for folder_delete, folder_publish, and folder_rename. These
  changes fix issue #216.
  http://dev.plone.org/plone/ticket/216
  [alecm]

- Added Topics to the default NavTree listing.
  [alecm]

- Made migration work from 2.0 svn, and not fail if SUPPRESS_ATCT_INSTALLATION
  is set.
  [alecm]

- Added RTL support (separate CSS is included for this, is only activated
  when the language is an RTL language).
  [limi] [mohsen]

- Added Mobile device support (handheld CSS profile).
  [limi]

- Fixed #2959 with a minor change to check_id to account for portal_factory
  weirdness. Also required an update to ATCT to do proper id checking on
  auto-rename.
  http://dev.plone.org/plone/ticket/2959
  [alecm]

- Re-did the fix for disappearing text in Internet Explorer, added special
  class 'visualIEFloatFix' that can be used for these, also adding a how-to
  with examples to plone.org.
  [limi]

- Added a reference rendering document to show all the user interface elements
  to ease cross-browser testing of third-party skins. Template name is
  'test_rendering'.
  [limi]

- Added ECMAUnit JavaScript testing framework to skins in anticipation of
  a real testSuite for the Plone JavaScripts.
  Pasted the license and credit files into the top of the library to keep
  them contained.
  [elvix]

- Made 'title' attribute on add-new-item drop down items display item
  description, as per bug #2938.
  http://dev.plone.org/plone/ticket/2938
  [optilude]

- Introduced the ExtensibleIndexableObjectWrapper. It's a wrapper based on
  the IndexableObjectWrapper for the catalog tool that can easily be
  extended by registering methods.
  [tiran]

- Renamed ugly 'PloneUtilities.py' module to 'utils.py'. The former is
  still around but issues a deprecation warning.
  [stefan]

- Fixed bug #3647 to allow removing all roles from a group.
  http://dev.plone.org/plone/ticket/3647
  [optilude]

- Fixed bug #3386. Modified folder_rename_form.pt to reflect user
  authorisations on each item.
  http://dev.plone.org/plone/ticket/3386
  [davconvent]

- Implemented fix for #3522 to add default groups "Reviewers" and
  "Administrators" to Plone, with the appropriate roles.
  http://dev.plone.org/plone/ticket/3522
  [dpunktnpunkt] [optilude]

- Made PloneFolder.moveObjectsByDelta not throw an error when passed a non
  contentish object id (apparently this happens during some migrations).
  Fixes #3959. Requires a small fix in AT done on 1.3 branch.
  http://dev.plone.org/plone/ticket/3959
  [alecm]

- Fixed computeRoleMap.py so that it stores the role information by
  user/group id not name, as a user and group may have the same name and
  it would be wrong to combine them.  This is related to issue #3711 which
  is itself a GRUF issue fixed in GRUF svn. Also implemented a faster sort
  algorithm in the above script.
  http://dev.plone.org/plone/ticket/3711
  [alecm]

- Made prev/next links in calendar portlet respect current query parameters.
  Fixes bug #3949.
  http://dev.plone.org/plone/ticket/3949
  [alecm]

- Added id="breadcrumbs-you-are-here" to the <span> tag where "you are
  here" is printed in global_pathbar.pt. It is now possible to remove
  cleanly that message, applying a CSS rule.
  [davconvent]

- Removed obsolete formtooltips member property.
  [stefan]

- Made all portal_status_messages with dynamic parts translatable.
  http://dev.plone.org/plone/ticket/2532
  [dpunktnpunkt]

- Included code from the CatalogOptimizer product, i.e. PLIP 89. This
  gives us DateIndexes and DateRangeIndexes instead of slow FieldIndexes.
  [stefan]

- Fixed bug in logged_in.py where login_password would not have been
  triggered even when appropriate on first login; fixed related issue in
  login_password.pt.
  [rafrombrc]

- Fixed problem where navtree was duplicate highlighting when user
  viewed home page, where folder default pages were showing up when
  'showAllParents' is True, general default page navtree fixes.
  [rafrombrc]

- Changed content_status_history to work w/ the new catalog-based
  folder contents code.
  [rafrombrc]

- Restored batchedFolderContents for backwards compatibility, and moved
  batching into the python script getFolderContents (which takes optional
  'batch' and 'b_size' parameters).  Marked batchedFolderContents and
  getFolderListingFolderContents as deprecated, both just call
  getFolderContents now.
  [alecm]

- queryCatalog was altering the queries passed to it to filter out types.
  This is unnecessary; it should only filter when no explicit types list is
  passed.  Also, queryCatalog is useful in places other than the search
  (folder_contents) where the filtering may be undesirable.  As a result
  the filtering is now optional and enabled by a parameter use_types_blacklist,
  which is used by default in search.pt and search_rss.dtml.
  [alecm]

- Added unit tests for folder based portal tabs and catalog based
  breadcrumbs.  Fixed bug in portal tab ordering.
  [alecm]

- Updated and enhanced the dependency checks to check for the right versions
  of Python, Zope and CMF.
  [tiran]

- Merged PLIP 74 - Cut/copy/paste actions on objects + Batch mode. The
  'contents' tab is now removed, though folder_contents can be accessed
  via the 'batch' button. It's importance is greatly reduced, because the
  most common operations it was being used for (cut/copy/paste and object)
  are now available directly as actions on the object.
  [davconvent] [optilude]

- Made sure migration catalogs the Members folder. This is required for the
  catalog-based navigation stuff.
  [stefan]

- Merged PLIP 76 - author feedback. A new link appears when viewing content
  created by portal members, taking the viewer to an author profile page.
  This page permits logged in users to send feedback via email (without
  exposing the author's email address) using a feedback form. It also shows
  the most recent publications by this member.
  [VladDrac] [optilude]

- Fixed link to CMF website on welcome page.
  [stefan]

- Merged plip91-folder-based-sections r6405:HEAD into 2.1 branch.
  [stefan]

- Implemented PLIP 91: Made sections (global tabs) render the top level
  folders in the portal root.  Removed existing actions for news and Members
  and added a news folder with default view set to news_listing.pt (formerly
  news.pt).  Added support for the property 'idsNotToList' from
  navtree_properties, so that the navtree and section tabs don't show the
  listed ids.  Added a catalog metadata column 'exclude_from_nav', so that
  when a boolean property of that name is set on an object it and it's
  children will be excluded from the navtree and section tabs.
  [alecm]

- Do not display "Forgot your password?" when user doesn't have
  "Mail forgotten password" permission.  Added a security check to
  RegistrationTool.mailPassword().
  http://dev.plone.org/plone/ticket/3338
  [dpunktnpunkt]

- Merged PLIP 75 - blacklisting of types. The types_not_searched property in
  site_properties can now be used to give a list of types which will be
  ignored for search purposes (via queryCatalog; the getUserFriendlyTypes()
  method in plone_utils can be used to get the same filtering elsewhere).
  [optilude] [jjmurre]

- Add new method to PloneTool getOwnerId, which gets the id of the owner
  of an object.  It's protected by the view permission on the object, and
  used in ownership_form in place of Creator, which may no be the same as
  owner for AT types.  Also modified ownership_form to use form controller.
  http://dev.plone.org/plone/ticket/3662
  [alecm]

- Set Title and description on member folders and personal folder.  Was
  broken due to permissions improvements in AT.
  [alecm]

- Merged plip93-optimize-templates r6360:HEAD into 2.1 branch.
  [stefan]

- Fixed #3779 - Removed worklist query from listFilteredActionsFor.
  http://dev.plone.org/plone/ticket/3779
  [alecm]

- Removed useless check for duplicate actions from listFilteredActionsFor.
  Gives a big speed improvement thanks to Dieter.
  [alecm]

- Minor refactoring of the calendar portlet to avoid unnecessary duplicate
  method calls.  Removed getBeginAndEndTimes.
  [alecm]

- Replaced breadcrumbs implementation with a faster simpler one based on
  ExtendedPathIndex.
  [alecm]

- Turned off DC MetaTags by default, added a global config to
  site_properties so that they can be re-enabled if desired.
  [alecm]

- Made the calendar portlet HTML output Not Suck. The code, however
  still does. ;)
  [limi]

- Fixed #3924 - eradicated all string exceptions.
  http://dev.plone.org/plone/ticket/3924
  [alecm]

- Fixed #3910 isValidEmail now uses the _checkEmail function from CMFDefault
  to avoid ValueErrors.
  http://dev.plone.org/plone/ticket/3910
  [alecm]

- Added empty fill-slot="sub" to discussion_reply_form to get rid of
  the second, broken 'add comment' button showing up on that form
  for top level comments, fixed #3845.
  http://dev.plone.org/plone/ticket/3845
  [rafrombrc]

- Moved retrieval of Zope system information out of
  plone_control_panel.pt and into proxied script getZopeInfo.py so
  that plone Managers who are not also Zope top-level Managers can
  view the page.
  [bmh]

- Added installation of default CSS and JavaScripts.
  [elvix]

- Added CSSRegistry and JSRegistry dependencies. All stylesheets and
  javascripts are now registered with these tools instead of hardlinked
  into header.pt.
  [elvix]

- Cut the default Styleesheets and Javascripts into smaller pieces to be
  served up by the CSS- and JS-Registries
  [elvix] [limi]

- Added showAllParents property to navtree_properties and to appropriate
  portal migration, added implementation to navtree code in PloneTool.
  [rafrombrc]

- Because normalizeISO() only deals with Unicode strings
  titleToNormalizedId() must make sure to pass it only Unicode. Added a
  check and a conversion from the site's default encoding.
  [stefan]

- Fixed UI task #21: renamed "Name" to "Login Name" in login form and
  portlet
  [mrtopf]

- Fixed UI task #19: default homepage for new members is not created
  anymore by default
  [mrtopf]

- Fixed UI task #5: Status message should show the name instead of
  title of a portal type on add. Now shows the title.
  [mrtopf]

- Fixed UI task #79: removed "you are logged in" message
  [mrtopf]

- Fixed UI task #73: added display of plone, zope and python version to
  the ControlPanel
  [mrtopf]

- Merged plip81-BylineHistory r6154:HEAD into 2.1 branch. This adds
  workflow history to the document byline.
  [stefan] [ender] [limi]

- Manually merged new css files from uiteam-plip85-componentized-css
  r6361:HEAD into 2.1 branch. These are not hooked up to anything just
  yet, but will be used by the CSSRegistry.
  [elvix]

- Split plone_javascripts.js into small components in preparation of the
  JSRegistry tool.
  [elvix]

- Merged uiteam-plip86-catalog-based-folder-listings r5865:HEAD into 2.1
  branch. Plone's folder_contents and folder_listing templates now use
  catalog results instead of traversal.
  [stefan] [alecm] [_ender_] [whit537]

- Added macros to folder_contents that allow reuse of the entire content
  area, including the definition of the content list.  Added slots and
  variables that allow macro users to change the title of the page, the
  columns displayed, and the type of content filtering and sorting
  performed.
  [alecm]

- Added slot to folder_listing that allows macro users to add custom
  bylines for specific types.  Also, added the ability to set a limit (in
  the request or containing template) on the number of items shown in a
  listing, along with a customizable link to see more contents which
  defaults to 'folder_contents'.
  [alecm]

- Merged uiteam-plip77-78-content-menu-browser-default-refactoring
  r6317:HEAD into 2.1 branch.
  [tiran]

  * PLIP 77: Constrain addable types on a per-folder basis
    New menu item "settings" on "add new item" drop-down to select
    which items to display, and how.
    [optilude]

  * PLIP 78: "Display" menu to select default view of a folder

    - Enable TemplateMixin and fix its UI (in ATContentTypes)
    - Add a "display" drop-down where these can be chosen
    - On folderish items, an option "select item" - shows browser, select
      default_page.

    [optilude] [davconvent]

- Cleaned up listMetaTypes by moving the payload into PloneTool and
  cleaning up the code.
  [tiran]

- Added PIL to dependencies to be able to close PLIP 82.
  [stefan]

- Changed 'context.aq_explicit.getObjectPosition' to
  'context.aq_inner.aq_explicit.getObjectPosition' in
  getObjPositionInParent.py to guarantee that we don't acquire
  getObjectPosition.
  [rafrombrc]

- Merged plip-80-navtree r6183:HEAD into 2.1 branch. This adds the new
  catalog-based navigation tree and sitemap. Plone now depends on the
  ExtendedPathIndex product.
  [stefan] [jladage] [tesdal] [elvix]

- Merged plip79-RelatedItems r6128:HEAD into 2.1 branch. Adds a macro to
  display related items in all content templates.
  [stefan] [_ender_] [mrtopf]

- Merged uiteam-plip73-sanitize-short-names r6113:HEAD into 2.1 branch.
  This removes "Allow editing of Short Names" from personal prefs and
  makes it a site-wide property.
  [stefan] [alecm]

- Merged plip72-LiveSearch r6110:HEAD into 2.1 branch. Adds LiveSearch by
  ObjectRealms to the search box.
  [stefan] [_ender_] [mrtopf]

- Merged plip71-full-screen-mode r6124:HEAD into 2.1 branch. This adds a
  document_action to enter full screen mode.
  [stefan] [arjen] [elvix]

- Use 'structure' in sendto_template.pt. Email text doesn't need any
  transforms.
  [panjunyong]

- Added some knobs to jscalendar:

  - show_hm: show hour and minute dropbox or not

  - show_jscalendar: show the jscalendar icon or not. If you hate the fat
    javascript, you can turn it off.

  - starting_year: starting year

  - ending_year: ending year

  - future_year: future years after this year

  - show_single_year: when year is fixed (min_year==max_year), sometimes
    we don't need to show the single year.
    [panjunyong]

- Old popup calendar (Plone 1.x) works again.
  [panjunyong]

- Don't install SecureMailHost if already installed.
  [tiran]

- Added 'SUPPRESS_ATCT_INSTALLATION' environment var check before ATCT
  installation. It can be set to 'YES' in order to suppress the
  installation of ATContentTypes at portal creation time for e.g.
  migration tests.
  [tiran]

- Use images in plone_tableless/colophon.pt just like the one in
  plone_templates.
  [panjunyong]

- Fixed ATContentTypes bug [ 1158950 ] ATTopic default view wrong.
  PloneUtils.browseDefault wasn't playing nice with folders and template
  mixin.
  [tiran]

   Alpha1 - Released March 12, 2005

- No longer uncatalog the Members folder on installation so that the new
  NavTreePortlet (not included) works out of the box.
  [stefan]

- Changed PloneTool.availableMIMETypes to use the MimetypesRegistry to
  return a list of mimetype names.
  [tiran]

- Fixed discussion_reply.cpy to use
  portal_discussion.getDiscussionFor(obj)
  instead of accessing the talkback object directly.
  [tiran]

- Now using CookedBody instead of EditableBody in news.pt
  [tiran]

- Merged Plone 2.1-atct branch. Plone now uses and requires
  Archetypes 1.3 and ATContentTypes.
  [stefan]

- Removed the debian directory.
  [stefan]

- Slight text edits in content_status_history template to more
  accurately reflect the influence of the effective and expiration
  dates.
  [rafrombrc]

- Added support for Firefox Live RSS Bookmark. RSS enabled objects
  will show the RSS button in firefox. Search results too.
  [batlogg]

- Fixed wrong i18n output encoding when create member area. We must set
  correct 'content-type' header to make PTS work when call translate.
  [panjunyong]

- Fixed PLIP16 integration to make it works with all content types, not
  limited to Plone Folder.
  [panjunyong]

- Added a charset header in sendto_template to make it work with
  PlasslessTranslationService. Previous sento_template didn't work with
  Chinese at least.
  [panjunyong]

- Members can be searched by group in folder_local_role and
  member_search_form now.
  [panjunyong]

- Moved the setting of login_time and last_login_time out of the
  (not always reached) login_success.pt and login_password.pt templates
  and into the (always executed) logged_in.py script.
  [rafrombrc]

- Permission settings were not being correctly copied to temp
  folder because we were using 'self' instead of 'intended_parent'
  for looking up permission roles, thus looking them in the factory
  tool instead of the target container.
  [sidnei]

- Fixed a long-standing visual styling bug of the 'hr' element, it used
  to only work properly with regards to colors/size in IE, now it works
  in standards-compliant browsers too.
  [limi]

- Added convenience ID for use in CSS - #portal-header - useful for background
  images in the portal header, for instance.
  [limi]

- Removed deprecated generateId script. We use generateUniqueId.
  [stefan]

- Added isRightToLeft utility Python Script which provides a fallback value if
  PTS is not installed or of the wrong version.
  [stefan]

- Merged in RTL support - Plone now correctly flips all the graphic
  elements and CSS declarations when using a right-to-left language like
  Arabic or Hebrew.
  [limi]

- Undid Jim's earlier change to the way the body tag is computed. It's
  now back to the original behaviour, with section-<section> class on
  the body tag.
  [limi]

- Fixed several potentially unsafe uses of acl_users.getUserById().
  [stefan]

- Integrated PLIP16. It is now possible to stop acquisition of local roles
  in a Plone Folder and change the roles of already assigned users/groups.
  Many thanks to: ender, MrTopf, hazmat and pjgrizel.
  [jladage]

- Plone now supports/requires GRUF 3.1.1. Thanks to pjgrizel for the patches.
  [jladage]

- Fixed #3641 - validate_start_end_date chopped off the AM/PM value when
  saving Events.
  http://dev.plone.org/plone/ticket/3641
  [stefan]

- Removed the dependency on Formulator as well as FormTool and NavigationTool.
  [stefan]

- It was impossible to create an item named 'index_html' in the portal
  root or inside a folder via WebDAV. Added a functional doctest for it.
  [sidnei]

- Removed headingFontBaseSize from base_properties and plone.css.dtml
  because it doesn't actually work and cost/benefit of implementation is too
  high.
  [whit537]

- Added utility javascript "nodeContained" to check if a node is contained
  in another node
  [elvix]

- Added Collapse/Expand-form-section javascript for future
  use. Usage described in plone_javascripts.js
  [elvix]

- check_id now accepts an additional 'contained_by' argument, allowing to
  disambiguate the target folder in cases where using the acquisition
  parent would yield the wrong results.
  [gkirk]

- Consolidated all monkey patches in the 'patches' sub-package.
  [stefan]

- Changed CatalogTool.catalog_object() and CatalogTool.reindexObject() to
  support the new update_metadata protocol (Zope > 2.6.2). An optional
  'update_metadata' argument controls whether the object's metadata record
  is updated while cataloging. It defaults to yes.
  [stefan]

- Plone now uses SecureMailHost instead of plain old MailHost.
  [tiran]

- SearchableText, Title, and Description now use TextIndexNG2 if installed.
  All three indexes fall back to ZCTextIndex if the TextIndexNG2 product is
  not installed. Note that in Plone 2.0 Title and Description used to be
  plain TextIndexes.
  [ajung]

- Plone now uses DateIndexes for created, modified, effective, and Date.
  Note that we do not yet use DateIndexes for expires (CEILING issues) and
  start/end dates of Events.
  [ajung]

- toLocalizedTime() replaced toPortalTime(). However this is NOT the way it
  should be and will be revised.
  http://dev.plone.org/plone/ticket/2461
  [db] [batlogg]

- getObjSize() now accepts second (optional) size argument to
  allow formatting of arbitrary sizes.
  [andym]


2.0.5 - Backed Up Willie - Released December 1, 2004
----------------------------------------------------

- Allow migrations to and from release candidates to finish. This was
  borked in RC2.
  [stefan]

- Fixed #3629 - Migration failed if 'Topic' portal type was missing or
  otherwise broken.
  http://dev.plone.org/plone/ticket/3629
  [stefan]

   RC2 - Released November 26, 2004

- Fixed #3612 - listFilteredActionsFor of ActionsTool now ignores missing or
  broken action providers.
  http://dev.plone.org/plone/ticket/3612
  [stefan]

- Fixed #3611 - Migration failed if the 'Folder' portal type did not have
  both 'edit' and 'local_roles' actions.
  http://dev.plone.org/plone/ticket/3611
  [stefan]

- Restored overridablity of left_slots/right_slots in folders by reverting
  the patch applied to fix #3472.
  http://dev.plone.org/plone/ticket/3472
  [stefan]

   RC1 - Released November 22, 2004

- Fixed it so the .error class no longer causes compression of items in
  forms.
  [limi]

- Fixed #3601 - Cancel in password_form redirected to the wrong page.
  Thanks to Varun for the patch.
  http://dev.plone.org/plone/ticket/3601
  [stefan]

- Fixed #3599 - Cancel in personalize_form redirected to the wrong page.
  Thanks to Varun for the patch.
  http://dev.plone.org/plone/ticket/3599
  [stefan]

- Fixed #3577 - Interchanged 'Edit' and 'Sharing' tab on folder. Thanks to
  Vamsi for the patch.
  http://dev.plone.org/plone/ticket/3577
  [jladage]

- Made prefs_error_log_form a tad safer in the face of weird upgrade issues.
  Also see #3435.
  http://dev.plone.org/plone/ticket/3435
  [stefan]

- Changed localLongTimeFormat to '%Y-%m-%d %H:%M'. Note: there is no migration,
  only new sites will be affected.
  [stefan]

- Fixed #3557 - Lines properties may still be lists if an old ZODB is
  upgraded to newer Zopes. Catching such a case in migrations. Thanks to
  Xenru for the patch.
  http://dev.plone.org/plone/ticket/3557
  [stefan]

- Fixed #2960 - The "Send this page to somebody" feature now uses the URL of
  the object including the view template. This avoids nasty login
  interactions when sending links to protected content.
  http://dev.plone.org/plone/ticket/2960
  [stefan] [sidnei]

- Made the column style sheet only apply to Screen, not Print/Presentation/
  Handheld.
  [limi]

- Massively simplified the print style sheet, should work much better in all
  browsers now.
  [limi]

- Moved ploneCustom to be the last of the CSS declarations, so you can easily
  do Print/Presentation/Handheld customizations in the ploneCustom.css now.
  [limi]

- Fixed Presentation stryle sheet to not show the site actions.
  [limi]

- More Google tweaking. Factored out the page title to a separate
  script and switched the order of the elements.
  [limi] [tesdal]

- Did a few things to improve the Google ranking of all Plone sites:
  Put all the style sheet declarations inside HTML comments, so Google
  doesn't try to interpret them as text, and removed the non-working
  meta links for author and copyright (scheduled for 2.1). Also
  changed the rel link for up to not show up if you are at the portal
  root.
  [limi]

- Plone was not showing the correct language in the header for an
  object, it was always using the site default, even if you had specified
  language on an object. Fixed.
  **NOTE:** This is a change to main_template, so if you have customized,
  you will probably want to copy in lines 8-9 from the new main_template.
  [limi] [tesdal]

- Caught additional IndexError/SyntaxError exceptions on
  isIDAutoGenerated.py to fix the case where a non-autogenerated-id
  starts with a valid portal_type name.
  [deo]

- Added i18n markup to global_siteactions.pt. Now those 'Small, Normal,
  Large Text' site actions can be translated.
  [deo]

- Changed imagePatch to use hasattr(aq_base(ob)...) and then
  getattr(ob, ...) in order to fix a problem with Archetypes
  ImageField which have a ComputedAttribute for
  title/alt. ComputedAttributes don't get computed on the
  absence of an acquisition wrapper.
  [sidnei]

- Fixed #3542 - queryCatalog script ignored 'sort_limit' argument. Thanks to
  kaib for the patch!
  http://dev.plone.org/plone/ticket/3542
  [stefan]

- Fixed #3541 - folder rename gave wrong error message. Thanks to Varun for
  the patch!
  http://dev.plone.org/plone/ticket/3541
  [stefan]

- Greatly improved the handling of DateTimeErrors in event_edit_form
  and metadata_edit_form + validators. No more traceback on Feb 31!
  [stefan]

- Fixed #2982 - the CMF does not allow to register with a user name that
  equals the name of a content object on the acquisition path. Provide a
  sane error message until this is resolved in CMF.
  http://dev.plone.org/plone/ticket/2982
  [rohrer]

- Fixed #3091 - new SetupWidgets can now work without cut/pasting the
  existing code, and use inheritance instead. Thanks to jccooper!
  http://dev.plone.org/plone/ticket/3091
  [limi]

- Implemented AM/PM support for the datetime-picker widget. Now, if
  your site_properties/localLongTimeFormat property contains the '%p'
  format specifier, the widget will display 12 hours and an additional
  AM/PM dropdown. Resolves #3264. Thanks to alecm for the patch.
  http://dev.plone.org/plone/ticket/3264
  [stefan]

- Fixed #3417 - because of acquisition, a user's name can not be the same as
  the portal name - this is now caught in the user registration validation
  instead of giving an error message. Thanks to kuru for the patch!
  http://dev.plone.org/plone/ticket/3417
  [limi]

- Fixed #2855 - Folders have "Properties" instead of "Edit" as title for
  the edit form.
  http://dev.plone.org/plone/ticket/2855
  [jladage]

- Fixed #2512 - folder_localrole_form role assignment pulldowns should be
  multiple select. Thanks to teix.
  http://dev.plone.org/plone/ticket/2512
  [deo]

- Fixed #2386 - Misc political incorrectness for msgid
  'help_search_keywords'.
  http://dev.plone.org/plone/ticket/2386
  [deo]

- Fixed #3142 - Swedish translation in search page translates "by" into
  "efter".
  http://dev.plone.org/plone/ticket/3142
  [deo]

- Fixed issues #3495, #3508 and #3509 - french translation errors.
  http://dev.plone.org/plone/ticket/3495
  http://dev.plone.org/plone/ticket/3508
  http://dev.plone.org/plone/ticket/3509
  [deo]

- Fixed #2171 - accessibility headers for the document actions were missing.
  http://dev.plone.org/plone/ticket/2171
  [limi]

- Removed the Add to Favorites icon from the breadcrumbs, since it is
  already in the document actions area. Favorites still suck, but will
  hopefully get some love in 2.1. ;)
  [limi]

- 'prefs_user_details' is now a Controller Page Template, and has better
  validation. Don't forget to re-customize if you have customized the
  old, non-cpt version.
  [geoffd]

- Fixed #3385 - tableless skin wasn't updated to the new header structure,
  causing the site actions to be positioned wrongly. This is an update to
  main_template for the people using tableless, please update your sites
  accordingly. Full explanation in the URL above.
  http://dev.plone.org/plone/ticket/3385
  [limi]

- Fixed #3429 - the section class was missing from the tableless skin.
  http://dev.plone.org/plone/ticket/3429
  [limi]

- Fixed #3086 - there is now an unRegisterPloneFunction in the
  plone_javascripts that allows you to unregister an onload event. Thanks to
  acamargo for the patch!
  http://dev.plone.org/plone/ticket/3086
  [limi]

- Fixed #3518 - Same issue as before, but for Images this time. Thanks to
  Varun for the patch.
  http://dev.plone.org/plone/ticket/3518
  [stefan]

- Fixed #3416 - Uploading a File with a bad name, without specifying an id
  in the form, caused validators to complain about 'id' instead of 'file'.
  This was especially bad as the current file_edit form does not show the
  'id' field at all :-P
  http://dev.plone.org/plone/ticket/3416
  [stefan]

- Fixed a usability bug where clicking the "Add default document"
  button would only generate a blank Document with the ID index_html
  - it now sends you to the edit form of said document instead.
  [limi]

- Fixed #3500 - Modified .metadata files to make FormController do something
  appropriate when someone submits a for using the return key in IE.
  http://dev.plone.org/plone/ticket/3500
  [geoffd]

- Fixed #3406 - Did a big makeover of FactoryTool.py that fixes a lot of
  permissions problems. Objects are now created after traversal so their
  owner and creator are set correctly. Parent folder permissions are copied
  to the TempFolder in which temporary objects are created, so temp object
  creation should behave the same way as regular object creation.
  ExternalMethods and scripts called with relative links are handed off to
  during traversal, so mapply headaches don't occur anymore. doCreate method
  now checks for and calls if present an object method called
  'manage_afterPortalFactoryCreate' so any extra post-instantiation
  initialization can take place.
  http://dev.plone.org/plone/ticket/3406
  [geoffd]

- Fixed #3458 - Images in folder_contents and navtree have wrong paths in
  VirtualHosted sites. It worked anyway because of acquisition, but is
  correct now. Thanks to mjm for the patch.
  http://dev.plone.org/plone/ticket/3458
  [limi]

- Fixed #3472 - you can now declare portlets on a template. Thanks to
  acamargo for the patch.
  http://dev.plone.org/plone/ticket/3472
  [limi]

- Fixed #3030 - content_status_modify.py now assembles the transaction note
  before performing the transaction. Thanks to raphael (Ritz?).
  http://dev.plone.org/plone/ticket/3030
  [stefan]

- Fixed #3457 - review portlet was not showing ID for items without Title.
  Thanks to Sjors for the patch.
  http://dev.plone.org/plone/ticket/3457
  [limi]

- Fixed #2857 - changed show_id.py to accommodate postback of a submitted id
  in the case where validation fails on the first edit of a newly created
  content object. Thanks to zenwryly.
  http://dev.plone.org/plone/ticket/2857
  [stefan]

- Fixed #3457 - review portlet was not showing ID for items without Title.
  Thanks to Sjors for the patch.
  http://dev.plone.org/plone/ticket/3457
  [limi]

- Fixed #3494. Description was used with 'structure' in some templates,
  notably news.pt and folder_listing. Note that Dublin Core defines this
  element as plain text. If your site relies on the old behavior refer to
  the patch in the issue. Patch by mathie, thanks.
  http://dev.plone.org/plone/ticket/3494
  [stefan]

- Fixed #2931. News items displayed "Read More" link even if there was
  nothing more to read. Thanks to mathie for the patch.
  http://dev.plone.org/plone/ticket/2931
  [stefan]

- Fixed #3457 - review portlet was not showing ID for items without Title.
  Thanks to Sjors for the patch.
  http://dev.plone.org/plone/ticket/3457
  [limi]

- Fixed #3038. Search terms "and", "or", and "not" are no longer highlighted
  in documents.
  http://dev.plone.org/plone/ticket/3038
  [rohrer]

- Made RegistrationTool reuse the EMAIL_RE regex from PloneTool instead of
  duplicating it.
  [stefan]

- Fixed #3447. Email address validation failed for upper-case characters.
  http://dev.plone.org/plone/ticket/3447
  [rohrer]

- Added border-collapse to the columns, so pixel/bitmap layouts that
  depend on the columns having 0 margin will work automatically. This
  is cleaner than the cellspacing="0" cellpadding="0" HTML approach
  that people seem to use. Fixes #3511.
  http://dev.plone.org/plone/ticket/3511
  [limi]

- Fixed HTML escape codes in password for special characters in
  registered_notify_template (#3499).
  http://dev.plone.org/plone/ticket/3499
  [jladage]

- Polished up the datetime-picker widget.  Now provides default values
  for month ('01') and day ('01').  Also new is the option to unset a
  date by deselecting the year ('----'). Fixes #2291.
  http://dev.plone.org/plone/ticket/2291
  [stefan]

- Made it so that headlines can't be obscured by the document action
  icons anymore.
  [limi]

- Made the check_id script work in the presence of incomplete
  Plone sites and missing permissions.
  [stefan]

- Fixed ownership on objects created by portal_factory.  The
  changes to portal_factory in 2.0.4 fix problems with mapply, but
  they mess up object ownership and potentially have side effects
  if an object tries to look up its owner during initialization.
  The pre-2.0.4 portal_factory breaks Epoz; the 2.0.4 portal_factory
  breaks PloneHelpCenter.  The current fix should enable both to
  work.  The Right Way to fix this would be to perform object
  construction in a post-traversal hook (pre-2.0.4 object construction
  happened at publication time; 2.0.4 constructs during traversal),
  but that means abandoning support for Zope 2.6.x.
  [geoffd]

- Added title attribute to links in action menus.
  [gotcha]

- Fixed transaction_notes overflowing struct size in ZODB.
  Also made there be 1 entry point into transaction_note instead
  of stray in PloneTool. Publishing hundreds of thousands of items
  would cause the trnx.description string to get larger than 65535
  which would cause FileStorage to fail on _notify
  [runyaga]


2.0.4 - Warp - Released August 16, 2004
---------------------------------------

- Fixed #3329. Results of breadcrumbs.py are no longer translated in
  global_pathbar.pt.
  http://dev.plone.org/plone/ticket/3329
  [stefan]

- Fixed #3332: hide the portal_siteactions from the print stylesheet.
  http://dev.plone.org/plone/ticket/3332
  [bmh]

- Fixed #3334. Added a break statement to the javascript for checking link
  protocols.
  http://dev.plone.org/plone/ticket/3334
  [bmh]

- Fixed #3325 and related. Plone calendar got confused when "datetime-format
  international" was set in zope.conf.
  http://dev.plone.org/plone/ticket/3325
  [stefan]

- login_form broke with Zope 2.7.2 because of stricter XHMTL parsing.
  [stefan]

- Fixed came_from testing when there is a query string (logged_in.py).
  [geoffd]

- Corrected some margins and padding, the content views and headline
  was very asymmetrical. Thanks to Brent for notifying me about this.
  She blinded me with science! ;)
  [limi]

- check_id script now rejects ids that are also catalog indices.
  [geoffd]

- Fixed portal_factory passthrough problem reported in #3243. Also
  portal_factory now logs exceptions during object creation (some were being
  swallowed higher up) (fix for #3148).
  http://dev.plone.org/plone/ticket/3148
  http://dev.plone.org/plone/ticket/3243
  [geoffd]

- Added enableHTTPCompression script and enabled HTTP compression for
  HTML, CSS, and JavaScript.
  [tiran]

- Fixed #3240 and related issues. Metadata elements like description and
  keywords (subject) could not be cleared.
  http://dev.plone.org/plone/ticket/3240
  [stefan]

- Merged fixes from tiran-plip30 branch. Changed PloneGenerator and
  MembershipTool.createMemberarea() to always use portal-aware factory
  methods for creating content. Prerequisite for future integration
  with ATContentTypes.
  [tiran]

- Changed the visual rendering of the nav tree. It now uses CSS instead
  of fixed values wherever possible.
  [limi]

  If you want the old look back, put the following in your
  ploneCustom.css::

    .currentNavItem,
    #portlet-navigation-tree a:hover {
    background-color: transparent;
    border: &dtml-borderWidth; &dtml-borderStyle; &dtml-backgroundColor;;
    }

    .currentNavItem {
    font-weight: bold;
    color: &dtml-fontColor;;
    }

    .navItem {
    padding: 0 0 0 20px;
    }

- Nav tree now displays Description for its items as a tooltip.
  [limi]

- Changed the behaviour of the site-wide actions (currently
  only used for text size) - so if you use or have a custom
  variant of this, you will need to re-customize this part.
  It was just too broken to not require template
  modification. It changed position in main_template, and
  produces more sane HTML now. Site actions have IDs now too.
  [limi]

- Changed the search box behaviour too - it shouldn't be
  absolutely positioned. If you have customized, you will need
  to move the main_template invocation of the search box, plus
  re-do the CSS, if any. Sanity was needed, sorry for the
  invonvenience.
  [limi]

- Added 'navtreeItem' and 'navLevelX' classes to the navigation
  tree, so it's possible to do funky stuff using only CSS to
  customizing the nav tree - for example make the only the
  top-level folders have bold text and dividers.
  [limi]

- Added 'navRootItem' and 'navItem' classes to facilitate better
  skinning of the nav tree.
  [limi]

- The body tag now has an HTML 'class'
  attribute, so you can skin different sections of the site
  with different styles. Prefix is "section-" and then the
  Short Name (partial URL) of the item in the root folder.
  This can easily be customized if you want this to
  work on all levels instead of just the root level, or to
  return multiple classes.
  [limi]

- Applied patch from #3159. Missing form fields should not cause user prefs
  to be set to None.
  http://dev.plone.org/plone/ticket/3159
  [stefan]

- Added a simple check for the existence of the template
  'global_languageselector' - this will allow the different
  multilingual implementations to hook into the area just below
  the documentActions to display language switchers. Macro name
  should be 'language' inside the template. See PloneLanguageTool
  for an example. This is the recommended location for language
  switchers.
  [limi]


2.0.3 - Noname - Released May 20, 2004
--------------------------------------

- Login portlet wasn't using the 'label' tag, corrected.
  [limi]

- Added id="portlet-related" in the Related portlet (was missing),
  and renamed 'portlet-recent-items' to 'portlet-recent' to make
  the name consistent with the other portlets.
  [limi]

- Hardened any send mail sending utilities and readying CMF 1.4.4.
  [andym]

- Fixed a small bug in plone_javascripts.js that prevents the highlight
  of the search term in simple searches.
  [azy]


2.0.2 - Hicks - Released May 13, 2004
-------------------------------------

- Added the 'listingNext' and 'listingPrevious' class for the batch
  navigator. The old span.next/previous will still work, but are
  deprecated. Please update any batch listings to the new format.
  [limi]

- Added a email address validator to the Plone tool and validate the email
  addresses for the send to feature, fix for #2975.
  http://dev.plone.org/plone/ticket/2975
  [tiran]

- Some templates were broken with Zope 2.6. Fixed by adding a
  surrounding metal:block with i18n:domain='plone' around colophon
  and footer.
  [sidnei]

- Moving definitions (webdav-locking) from edit-templates to
  global_defines, where they belong.
  [limi]

- Added missing definition of filterOut.
  [ajung]

- Removed unnecessary hook in FactoryTool that is handled by Archetypes
  itself now.
  [deo]

- Default position of the "Recent" portlet is now on the left.
  [limi]

- Added a new variable 'current_page_url' to 'global_defines'. Since it's
  pretty much impossible to get the correct URL to the current page once
  you're inside CMF, the base tag and Zope and a VHM, I added this
  convenience variable. For those who are curious, here's how it looks:
  'current_page_url request/VIRTUAL_URL|string:${request/SERVER_URL}${request/PATH_TRANSLATED}'
  Easy, eh? Updated the Plone templates to use this variable instead. Use
  this if you need a variable to use with HTML anchors, it will give you
  the actual URL that is currently being displayed in your browser.
  [limi]

- Default text on member pages are now disabled, since it just pollutes the
  search results. You can insert the default text in 'homePageText.pt' like
  before, the only difference is that it's disabled by default, and uses
  Plone's built-in mechanism to show relevant help text if you're the owner
  of the document instead.
  [limi]

- Added scoring details + i18n information in the search results. Thanks
  to Andrew Veitch for the suggestion.
  [limi]

- Renamed METAL macro "list-item" to "listitem" in news.pt and folder_listing.pt
  to fix Zope 2.6 compatibility.
  [limi]

- Commented out the javascript that auto-focuses on the first field in a form.
  There are too many places that causes a lot of trouble by moving focus away from
  a field in which the user is actually typing.
  [elvix]


2.0.1 - Jello - Released May 4, 2004
------------------------------------

- Backported fix for #2183 from HEAD. _verifyObjectPaste() should deny
  pasting if the content type is not allowed in the target container.
  http://dev.plone.org/plone/ticket/2183
  [stefan]

- Improvement to Customization policy:
  In a customization policy class you can now provide an optional method
  'getPloneGenerator',
  where you can return a different PloneGenerator than the default one
  Affected files: Portal.py, CustomizationPolicy.py,
  interfaces/CustomizationPolicy.py
  [zwork]

- Fixed #2973. Try to avoid brain.getObject() to speed up plone.
  http://dev.plone.org/plone/ticket/2973
  [tiran]

- Fixed #2795. Replaced aq_explicit by aq_inner in batchedFolderContents.py.
  http://dev.plone.org/plone/ticket/2795
  [tiran]

- Fixed #472. Discussion now uses CMFFormController and subject/body are
  required fields now.
  http://dev.plone.org/plone/ticket/472
  [mrtopf]

- Portal.py/SkinsTool.py: Removed monkey patch that renamed the skin request var to
  plone_skin and moved request_varname to our SkinsTool
  [tiran]

- Fixed #2583. Disable submit button when item is locked and add a locked
  icon next to the disabled submit button.
  http://dev.plone.org/plone/ticket/2583
  [tiran]

- Fixed #2826. searchterm-highlighting now functions correctly, it
  highlights text in the fuill content-area, but only highlights the parts
  it is supposed to highlight.
  http://dev.plone.org/plone/ticket/2826
  [elvix]

- Fixed #2691 - External-link-detector javascript is now case-insensitive.
  http://dev.plone.org/plone/ticket/2691
  [elvix]

- Fixed #3001 - Fallback handling to avoid javascript-error-messages in IE5.
  http://dev.plone.org/plone/ticket/3001
  [elvix]

- Fixed #2859 - plonifyActions accepts javascript urls.
  http://dev.plone.org/plone/ticket/2859
  [tiran]

- Fixed #2948 - Auto generated ids are now lower case and the number is more
  random.
  http://dev.plone.org/plone/ticket/2948
  [tiran]

- Fixed #2990 - Nested groups don't break the prefs_group_members template
  any more.
  http://dev.plone.org/plone/ticket/2990
  [tiran]

- Fixed #3005 by catching non existing home folder.
  http://dev.plone.org/plone/ticket/3005
  [tiran]

- Fixed #2963 - Allow access to Products.ZCTextIndex.ParseTree.ParseError
  and catch it in the queryCatalog script.
  http://dev.plone.org/plone/ticket/2963
  [tiran]

- Fixed #2862 - Added a listMetaTags script to skins/plone_scripts to add
  automagically generated meta tags in the '<head>' tag.
  http://dev.plone.org/plone/ticket/2862
  [tiran]

- Fixed #2821 - The user doesn't show up as a member of that group after
  adding because the template was returned in the same transaction. Now the
  add/delete script is using a redirect.
  http://dev.plone.org/plone/ticket/2821
  [tiran]

- Fixed #2876 - Folder rename does not reindex title. Added a explicit
  reindex if only the title has been changed.
  http://dev.plone.org/plone/ticket/2876
  [tiran]

- Fixed #2892 by using global_defines in the calendar_popup template.
  http://dev.plone.org/plone/ticket/2892
  [tiran]

- Fixed #2749 - 'groups' wasn't initialized as an instance variable, so any
  changes to it would vanish on restart.
  http://dev.plone.org/plone/ticket/2749
  [sidnei]

- Fixed #2671 - default_page as a string property would not work. Fixed this
  and added tests for basic behavior. More tests are needed IMHO.
  http://dev.plone.org/plone/ticket/2671
  [sidnei]

- Fixes for #2914. Although I could not reproduce. We now have a unit test
  showing that this behavior should not regress. Some logic in PloneTool
  was changed.
  http://dev.plone.org/plone/ticket/2914
  [runyaga]

- Fixed #2814 - 'Document' was being checked against a list of
  FactoryTypeInformation, which would never work. Changed to check against
  the list of portal_types generated by '<FTI>.getId()'.
  http://dev.plone.org/plone/ticket/2814
  [sidnei]

- Fixed #2907 - 'get_size' can return long. Also, improved the script a bit
  to be more correct with regard to sizes, include GB, use 'kB' instead of
  'K' (which stands for Kelvin), return '0 kb' if size is null or 0, and add
  tests for all of this.
  http://dev.plone.org/plone/ticket/2907
  [sidnei]

- Fixed #2998 - The types tool has a getTypeInfo method, but with different
  signature.
  http://dev.plone.org/plone/ticket/2998
  [stefan]

- If toolicon can't be found, it may be because a tool is
  inheriting from a Plone tool, so the icon path (which defaults
  to relative to CMFPlone's dir) is invalid. We fallback to
  resolving the CMFPlone dir and join the path.
  [sidnei]

- added a PloneBaseTool that all other tools inherit
  from. Currently this does absolutely nothing, just a placeholder.
  [tiran]

- changed the registration of tools to provide different images in the ZMI
  [tesdal] [limi]

- validate_document_edit assumed the Content-Type header is always
  present. This is not the case.
  [stefan]

- Fixed #2980 - Handle dates between PLONE_CEILING and CMF_CEILING.
  http://dev.plone.org/plone/ticket/2980
  [tesdal]

- Added two classes to allow list without markers:
  'ul.visualNoMarker' and 'ol.visualNoMarker'.
  [limi]

- Added Full Screen view for images.
  [limi]

- Implemented 'management_page_charset' as ComputedAttribute returning the
  value of portal_properties/site_properties/default_charset. Also see #2778
  This means Unicode characters are shown correctly in the ZMI too.
  http://dev.plone.org/plone/ticket/2778
  [stefan]

- Added years range properties in site_properties:
  [deo]

  - calendar_starting_year: (default: 1999), the fixed minimum year
    displayed on calendar widgets

  - calendar_future_years_available: (default: 5), how many years
    (from current year) are displayed on calendar widgets

- Added a 'portlet_prefs' that displays the different prefs panels
  available once you're inside the prefs area. This uses the portlet
  slots introduced below.
  [limi]

- Added 'portlets_one_slot' and 'portlets_two_slot' to make it
  possible to fill the portlets areas with content. This way, you
  don't have to know what kind of layout you are in.
  [limi]

- Plone now supports translation of keywords and other metadata.
  There is a separate i18n:domain for this - 'plone-metadata'.
  Anything added into a (for example) 'plone-metadata-fr.po' file
  with the 'plone-metadata' domain will
  be parsed on the metadata_edit_form in French, and replaced with the
  translated strings from the po-file. Please note that this usually
  requires adding new metadata in a default language to avoid
  a mess when translating. Plone does nothing to enforce this at the
  moment. Currently supported fields are Keywords (aka. Subject) and
  Copyright (aka. Rights). The 'search_form' was also updated.
  [limi]

- Added a define-macro "list-item" to news.pt and folder_listing.pt, so
  they can be reused in other templates. You have to define a repeat
  statement outside it similar to the template in
  'plone_templates/news.pt'. The macro itself renders one item.
  [limi]

- Added icons for left/leftmost/right/rightmost. Removed unused icons.
  Fixed alt-representations of images.
  [limi]

- Fixed bare 'except:' statements in Plone so we don't swallow
  ZODB ConflictErrors. Mostly by adding 'except ConflictError: raise'.
  [stefan]

- Inserted a metal definition that enables the folder_listing to be
  used from other templates. [limi]
  Example:

  '<div metal:use-macro="context/folder_listing/macros/listing">
  The folder listing of the current folder
  </div>'


2.0 - Fyuti - Released March 23, 2004
-------------------------------------

   Final

- Fixed #2852.
  http://dev.plone.org/plone/ticket/2852
  [geoffd]

- Added cleanupSkinPath method to migration_util, used to remove
  bad skin layers when adding the Plone Tableless skin in the RC5-RC6
  migration.
  [geoffd] [tiran]

- Updated link in footer.pt to Alan's new company.
  [andym]

- Added 'domain' parameter to translate.py. Defaults to 'plone'.
  [deo]

- Updated isExpired.py to take the case that datetime instances
  are not callable.  It looks a bit strange.  But its fixed.
  Future versions should use ExpirationDate accessor.
  [runyaga]

- The tableless skin didn't have the top_slot defined.
  [limi]

- Fix WebDAV for the nth time. browserDefault was using the
  portal_utils tool as the context for all DAV requests, instead
  of the real object.
  [sidnei]

- Fixed #2808 - metadata_edit form was broken when the date format was set
  to international (zope 2.7). Fixed date_components_support.py
  http://dev.plone.org/plone/ticket/2808
  [tiran]

- Fixed #2804 - plone_memberprefs_panel.pt ignored the 'visible' of
  configlet actions. that's corrected now.
  http://dev.plone.org/plone/ticket/2804
  [zworkb]

- breadcrumbs.py had bugs in which (1) a terminal object was sometimes
  displayed twice, and (2) terminal non-content non-view objects (e.g. page
  templates) were not displayed at all.  The bugs have been fixed and
  breadcrumbs.py has been refactored a bit to make the source easier to
  understand and maintain.
  [geoffd]

- Fixed some instances of 'disable_border' being written as 'disable_border1'
  [limi]

   RC6

- Make portal more tolerant if admin removes cookie_authentication
  object which enables form-based logins.  This is a response to
  http://article.gmane.org/gmane.comp.web.zope.plone.user/13868
  It does not full fix, just a hold over until it is addressed
  properly.
  [runyaga]

- Fix for #2769 - You could not enable/disable green 'editable border'
  because this was being done in the 'head_slot' which corresponds to
  '<head>' in the document. Control of the border is computed in
  global_defines.pt which is the first macro used in main_template.
  Introduced another slot in main_template called 'top_slot' which occurs
  before global_defines. *All third-party products will have to fill
  'top_slot' instead of the 'head_slot' to disable the borders, the syntax
  apart from that is identical.*
  http://dev.plone.org/plone/ticket/2769
  [runyaga]

- Fixed #2744 - Large Plone Folders should use folder_workflow. Fixed
  PortalGenerator and added migration and tests.
  http://dev.plone.org/plone/ticket/2744
  [stefan]

- Fixed and re-fixed #2246 - Short name should be editable without
  specifying a file.
  http://dev.plone.org/plone/ticket/2246
  [achilles] [stefan]

- Added a monkey-patch workaround for #1323. This *may* be considered a CMF
  bug. See setFormatPatch.py.
  http://dev.plone.org/plone/ticket/1323
  [stefan]

- Moved 'document_byline' and 'document_actions' to the
  'plone_content' folder - as they belong to the content templates.
  [limi]

- Checked in fix for 2600: group names and user names were not
  shown correctly in the Group Memberships form and the Members of
  Group from, if viewed not in english. Fix Suggested by ozone.
  [jok2]

- Fix for 2704: added manager proxy role to register.cpy to avoid
  error if mail could not be sent to new member. Fix suggested by
  Seb Potter
  [jok2]

- Fix for 2462: change default value of ids to empty list instead
  of None (folder_delete.cpy). Done to avoid error about iteration
  over non-sequence, if no item is selected for deletion. Fix
  suggested by Seb Potter
  [jok2]

- Merge the fix for portlet_related over from the microoptimisations
  branch and fix for 2293 and 1920
  [andym]

- Split 'use_folder_contents' site property into two different
  properties: typesLinkToFolderContents (a navtree prop for
  how nav tree behaves) and typesLinkToFolderContentsInFC
  (a site-wide prop, for how folder_contents page should
  behave). Added migration to create these two and to remove
  the old use_folder_contents.
  [pupq]

- Diet Plone - an initial page load of Plone was reduced from
  150K to 75K, and HTTP requests from 30 to 15 by performing
  the following tweaks:
  [limi]

  - Calendar JS only included on pages that use it

  - Deprecated pop-up tool tips JS code commented out
    (easy to re-enable if you need it for legacy sites)

  - Made the colophon buttons with CSS instead of using images

  - Pulldown menu only available to logged-in users
    (although it can be enabled for anonymous too, if you need it)


- Added fix for the bug reported by Edward Muller (skin setting
  and login problems). Don't clear the name of the skin cookie
  in the prefs_portal_skiset.py. [jok2]

- Added fix for breadcrumbs so that the parent folder is shown when
  you are looking at folder_contents.  [pupq]

- Fix bug 2373 so folder_contents items goto
  getTypeInfo.getActionById('view')
  [runyaga]

- Removed the ability to edit short names while adding a file,
  since users have problems remembering that the extension has to be
  included. They are also very surprised when the file they uploaded
  has a different file name. Removing this will give them a sensible
  default. If you want to re-enable short names for files for your
  site, remove the comments around the code.
  [limi]

- Added the Creator/Modified indicator to the edit forms too.
  [limi]

- Added security checks for viewing the view forms. There was no
  security problem, since you couldn't save the document, but now we
  also check that you are logged in, so you can't invoke the URL
  directly to look at the edit form anymore either.

- Added getAllowedTypes for use in folder_contents and global_contentmenu
  to check for getNotAddableTypes and when to show a single item instead
  of a dropdown. ( fixes bug )

- If a content type is listed in
  portal_properties/site_properties/use_folder_contents then use
  'folder_contents' to display it, not ''. Removed the migration
  that initialized this value to ['Folder']
  [pupq]

   RC5

- Removed false 'required' indicators for Title attribute on file/image
  edit forms.  You simply need to upload a file.  That's it.
  [runyaga]

- Added extra check for dictionary-based actions. Will work better
  with old sites being migrated.
  [tesdal]

- The base slots were being filled in the wrong order, causing it to
  not work as expected. Fixed.
  [tesdal]

- Added macro names for the left/right slots, so you can override them
  by filling the slots from a template. Example:

  '<metal:override fill-slot="column_one_slot" />'
  '<metal:override fill-slot="column_two_slot" />'

  This enables you to "turn off" the slots from a template, thus
  eliminating the need to create a folder to do it.
  [limi] [tesdal]

   RC4

- CMFPlone.FormTool.BasicForm.get_field signature has changed.
  def get_field(self, id):
  to
  def get_field(self, id, include_disabled=0):
  FormTool is deprecated or will be deprecated in 2.0. Bug #2498
  http://dev.plone.org/plone/ticket/2498

- For those of you who were running tableless designs in the RC3
  and earlier releases and want to keep it that way - simply add
  a DirectoryView for 'plone_tableless' in 'portal_skins', and
  add it to the skinpath. This will activate the tableless versions
  of:

  - main_template

  - ploneColumns.css

  Apart from adding these two, no other changes are needed. The reason for
  this change were numerous, the most important ones being crash bugs in IE
  and bugs in Safari. Tableless will probably return as the default if we can
  get it stable enough, but it wasn't good enough for 2.0.
  [limi]

- Made sure there are no naked mailto: links for spambots, all mail addresses
  are now using the spamProtect script. Syntax:
  '<a tal:replace="structure python: context.spamProtect(Person.email)" />'
  - this will return a complete a href tag with the mail address spam-
  protected. [limi]

   RC3

- WARNING: Some changes had to be made permission-wise to make the default
  behaviour make sense. It was very inconsistent in 1.0, and we decided to do
  a partial clean-up so it behaves better in 2.0. Read this and make the
  necessary changes to your application, especially if you use the List Folder
  Contents permission in special ways. The following changes were made:

  - 'folder_listing' is not governed by the List Folder Contents permission
    anymore, which is the correct behaviour. The best way to think of
    'folder_listing' is as an alternative 'View', *not* as an alternative
    'folder_contents'. 'folder_contents' is for editing and manipulating the
    contents of a folder, not for viewing.

  - 'folder_listing' is now always available, *but* checks for permissions,
    and hides content you don't have the permissions to see.

  - You still can't access a 'private' object, so it's still protected, no
    change there.

  - The one potential problem is that it's possible to see the ID of an object
    - this is because of the way CMF and Zope does it however - and you have
    to know the exact method call to do this. It will never give you anything
    but the ID though, so we don't view this as a big problem.

  - 'visible' content is also visible to anonymous users. This was the
    original intent of the state, but was broken in 1.0. However, if you
    depend on this behaviour, you should note that it has changes, and make
    your own custom workflow for this.

  - Finally, this thing needs to be tested properly, so please help out by
    installing third-party applications and see if they are affected in a
    negative way by this change.

- checkPermission is exposed in global_defines.  We check to see if you
  can Modify portal content in folder_contents to determine whether or not
  to show the external editor icon.  Changes references to
  portal_membship.checkPermission to use the global checkPermission reference

- Do not show order column if you can not Modify portal content for
  folder.

- [FEATURE] Added 'sharing' action for all nonFolderish types in portal_types
  If you have a problem with this bring it up w/ alex or dannyb

- If you have any object actions besides 'view' you will not get the
  greenborder.  before we suppressed if it was 'view' or 'folderContents'

- Permissions changes.  The folder_buttons, copy,paste,rename,delete,cut
  were protected by CMFCorePermission.ModifyPortalContent which is
  incorrect.  Moved it to AccessControl.Permissions.copy_or_move.  I am
  not sure that is correct either because all permissions checking for
  folder_buttons is done at the folder level.  If we want to be more
  fine grain (show a delete button if we have access to any content to
  delete) we will need to execute a condition (script) for all content.
  This could be prohibitively expensive.  Changes made in
  CMFPlone/setup/ConfigurationMethods.py

  - It was possible to delete something out of a folder even if you
    did not have 'Delete objects' permission.  If you 'cut' a object
    from one folder and pasted it into another.  So we put an extra
    condition on 'cut', python:portal.portal_membership.checkPermission(
    'Delete objects', object)

  - We should wipe out all actions and reinstall them that are
    regarding the 'folder_buttons' category

  - This is in regards to issue, #1985

  - Declared manage_copyObjects on PloneFolder.PloneFolder protected
    by 'Copy or Move' instead of 'Modify portal content'

- moved CMFPlone/migrations files into CMFPlone/migrations/v1 or v2
  modules.   Although this is not a permanent solution.  It will work
  well enough.

- allowedContentTypes is a expensive call.  made this global inside of
  plone_templates/global_contentviews.pt and its reused throughout the
  global_contentmenu, global_contentviews and folder_contents. This
  should make the experience a tad snappier

   RC2

- Renamed portal_control_panel_actions to 'portal_controlpanel' and made
  it use ToolNames instead of hardcoded strings.
  This will break RC1 sites, so here's how to update your existing site:

  - Delete all ActionIcons with category "controlpanel"

  - Delete the portal_control_panel_actions tool

  - Add Plone Tool - Plone Control Panel Tool

  - Invoke the following URL:
    http://mysite/portal_controlpanel/registerDefaultConfiglets

- Now comments in Plone are text/plain.  No longer using structured-text.
  DiscussionTool has grown a method, cookReply.  This is temp fix.
  CMFDefault.Document should have a cook method which can 'recook' its
  body text.  This is something Archetypes should implement.  Being able
  to recook without passing in the values.
  Modified CMFDefault to accept a text-format in createReply.

- Add 'site_actions' category to portal_actions.  This includes:
  Small, Normal, Large text links.  This was added in
  setup/ConfigurationMethods.py addSiteActions.  We add 3 actions to
  portal_actions and 3 icons to portal_actionicons.  NOTE:  We want
  to cache the icons in the plone_utils.getIconFor -- this is a problem.
  If you change an icon it will not take effect until you restart zope.

- Now in setup/ConfigurationMethods.py where the left/right_slots for the
  portal root are created have been changed.  It is quite sensible.  We
  are removing the terminology of 'slots'.  We are moving towards the
  preferred naming, 'portlets'.  Macro paths are sensible:
  context/portlet_foo/macros/portlet
  This means that all slots are now renamed portlet_$name and all macro have
  been renamed to 'portlet'.  The old slot code still exists and has
  deprecation comments in the PageTemplates.

   RC1

- PrivatePloneWorkflow and PrivateFolderWorkflow no longer register their
  workflow factories. They will disappear from Plone core.
  [stefan]

- Fixed PloneWorkflow's mapping of ChangeEvents permission to follow the
  mappings for ModifyPortalContent.
  [stefan]

- Made ListFolderContents unavailable to Members when a folder is in the
  private state (FolderWorkflow).
  [stefan]

   Beta 3

- WARNING! If you attempt to add several Plone sites back-to-back you will
  encounter some problems.  The system works fine for adding a single
  Plone site.  If you want to add more you will have to restart your Zope.
  We have worked out the problem and its not too difficult we just need
  to put a solution in place.  Thanks to Steve Alexander and Tres Seaver
  for helping out. In summary, we know there is a problem.  Please do
  not bug us.  We are attempting to adhere to the mantra,
  'release early, release often.'

- Deprecated stylesheet_properties for the new base_properties in the CSS.
  This one is much more flexible, clean and reusable, but note that if your
  site relied a lot on the old stylesheet_properties file, you will have to
  move the attributes to the new file. The reason for renaming it was to not
  cause errors when upgrading. It will reset your color choices, though.
  The new properties are documented in ploneCustom.css.
  [limi]

- Removed the CMFWiki and CMFCollector skins from Plone core.
  **NOTE:** You need to add the correct skin paths if you are using
  these products, they are no longer installed by default. The skins
  are now located inside the Products themselves.
  [limi]

- Added version checking of Products, and easy reinstall from Add/Remove
  Products panel.
  [zwork] [limi]

- Hooked up the plone_memberprefs_panel for easy adding of user-specific
  control panels.
  [ronnix] [andym] [limi]

- Portlets overhaul and renaming, in separate directory now.
  [limi]

- Removed XML-RPC from Add Comment form.
  [limi]

- Renamed "Name" to "Short Name" in the edit forms.
  [limi]

- Moved all the skins to PloneSkins in the Collective.
  [limi]

- got rid of the ancient, nasty FormulatorTool. [geoffd]

- fixed portal_factory so that the folder and folder_url values provided to
  actions are correct for temporary objects, made content_status_modify and
  metadata_edit portal_factory aware.  objects created with portal_factory
  should now behave just like normal objects. [geoffd]

- renamed plone_debug script to plone_log.  if you want to log out to zLOG
  simply context.plone_log('this should be in the log')

- removed 'portal_workflow' from list of portal_actions' Action Providers.
  Sites with large worklists would benefit most from this.  We no longer
  put worklist states in the 'personalBar'.  We use the 'review_slot'.

   Beta 2

- now shipping with Formulator 1.5

- add portal_actionicons.renderActionIcon(category, iconid, default)
  which returns back the actual object instance instead of a path.
  Now you can put icon and action in the bar left of the 'add new item'
  in the green bar by:

  * creating an action who's category is: object_actions

  * create an action_icon whose category is: object_actions
    and icon_id is the same as the 'id' above

  this potentially invokes lots of calls down to portal_actionicons
  but its the only way to actually get the icons with all the attributes.
  We could cache the icons in the renderActionIcon method.  Also added
  unit tests.

- add PloneContent.py base class that inherients from PortalContent
  we could use this in the future to hook the reference engine in
  archetypes (or rather the reference engine that should move out
  of archetypes *wink*)

- added 'enable_border' to folder_localrole_form, folder_edit_form,
  content_status_history so that the greenborder will show up when
  you are performing these actions at the root of the Plone site.
  this should be done in python instead of in the templates.  2.1 ;-)

- added 'unwrapobjects' property to the CatalogTool PropertyManager
  if this is True the catalog will unwrap the AcquisitionWrapper from
  the object before indexing.  This was done because you could get
  unexpected results if you had content with the same ID as a Index.
  [stefan removed this because runyaga sucks but we need this w/ tests]

- added a Plone Site portal_type.  This portal_type is what the root
  of the Plone Site's _setPortalTypeName is set to.  This way the
  Folder permissions are manipulated separately from the root of
  the Portal.  What became a major problem in "private" sites was
  having a different policy set in the Permissions tab but then
  someone "Updating Permissions" from the workflow tool which would
  reset the permission on the root of your site!  This is added to
  migrations.

  * If you only allow 'Authenticated' to 'View' the portal root
    when you login you authenticate but get a 'Insufficient Privs'
    page.

  * It seems you can not logout ;-( -- maybe you logout but
    before redirection you dont have 'View' permissions and the
    exception rollsback the logout?


- personalBar (mystuff, preferences, undo, logout) now no longer uses
  'global' actions.  This was causing worklist 'pending <foo> (N)' in
  the personalBar.  Which is not i18nable and breaks semantics of
  the personalBar (which are user-centric actions).  Two things were
  introduced:

  * keyFilteredActions which will return a two dimensional dictionary
    keyed_actions=[category][action_id] so you can easily pick out actions
    using its category and id.

  * getOrderedUserActions which given a two dimensional dictionary
    keyed like keyFilteredActions and a ordering dictionary will return
    'in order' the user actions.  If you add more actions using tools
    they will show up in between the 'pre','post' ordering lists (which
    can be passed ala ordering dictionary)

  NOTE:

  * portal_undo actions 'undo' category should be 'user' not 'global'
    this goes the same for portal_properties' 'configPortal' action

  * plone should not ship with 'default_workflow' which injects
    hardcoded information into the listFilteredActionsFor.

  * all worklists in plone workflows should not use 'global' category
    but should use the 'workflow' or 'worklist' category.  Up to whoever
    gets to it first 8-).

- Presentation mode now renders paragraph tags invisible, which means
  you can create a richer document for web and/or print, but keep the
  presentations without the additional comments. If you want the old
  behaviour, just uncomment the relevant p {} section in the
  plonePresentation.css style sheet.

- CMFPlone.Portal.Site now uses the OrderedContainer mixin.
  __implements__ the OrderContainer and DefaultDublinCoreImpl xface.

   Beta 1

- Content types in Plone now have the notion of both Views and
  Actions. Actions are show on the content bar, views are tabs, as
  earlier.
  [limi]

- Reworked the way Content Views are constructed - now you can have
  multiple content areas with tabs on one page. Idea by [arnia],
  implementation by [limi].

- Reworked the default content views, they look much better now.
  [limi]

- Moved the byline to a separate template in plone_contents.
  [limi]

- Cache headers were moved to a separate file in plone_templates called
  global_cache_settings to make it easier to customize the caching options
  without changing main_template.
  [limi]

- GroupUserFolders' GroupsTool and GroupDataTool are now subclassed in
  CMFPlone [runyaga]

- QuickInstallerTool is now installed in
  CMFPlone/Portal/PortalGenerator.setupTools()
  In the migrations for 1.1 QuickInstaller is notified that are installing
  CMFActionIcons and CMFCalendar outside the framework.  Now they show
  installed.  QuickInstaller is now subclassed in Plone and has a test
  that installs/uninstalls a product.  [runyaga]

- CatalogTool's searchResults takes Permission settings acquired through
  local groups into account. Permission local roles assigned to users
  is still not honoured.
  [_robert_]

- MembershipTool's listMembers and listMemberIds now only return real users
  (not groups) when GRUF is employed. The MembershipTool comes with tests!
  [_robert_] [stefan]

- Added a ZopeTestCase based test framework developed at the Castle Sprint.
  Nuked the old tests (with Sidnei's permission).
  [stefan]

- Removed Domains from the user preferences - this field makes it very easy
  to lock yourself out of your account, and should therefore only be
  available to administrators.
  [limi]

- Bug fix for #1154 - SearchableText should be ZCTextIndex.
  http://dev.plone.org/plone/ticket/1154
  [kapil]

- Added unicode splitter for zctextindex element pipeline from silva
  (w/ license).
  [kapil]

- Added lexicon addition to migration.
  [kapil]

- Added lexicon addition and recreation of searchabletext index as zctext to catalog
  tool's manage_afterAdd.
  [kapil]

- Added new directories: 'plone_portlets' (formerly 'plone_templates/ui_slots'),
  'plone_form_scripts' (formerly 'plone_scripts/form_scripts') - these two to
  avoid having skin paths two levels deep - 'cmf_legacy'
  (contains the few CMF scripts we still depend on), and 'plone_prefs' (contains
  the new Plone Control Panel). Skin paths updated.
  [limi] [runyaga]

- Location is now shown in the events box.
  [limi]

- External Links in the default folder view now go directly to the URL specified.
  [limi]

- Events now show location and from/to-date in the default folder view.
  [limi]

- Changed the behaviour of deleting objects in PloneFolder, so the object is
  checked for the Delete Object permission instead of the folder. This means
  that the workflow can restrict the Owner from deleting an object (for example
  in a published state).
  [sidnei]

- Subclassed all CMFCore and CMFDefault tools for easier extension in the future.
  [sidnei]

- generateUniqueId and isIDUnique now are a bit more unique (with regards to
  randomness) and we now suffix generated ID's with .html - issue #1343
  http://dev.plone.org/plone/ticket/1343
  [runyaga]

- Added Recently Published slot, and a complimentary Archive page.
  [limi]

- Changed the comment structure and layout - it's much moresimple and
  elegant now.
  [limi]

- Added permanent CSS fix for the Internet Explorer 6 Disappearing Elements
  bug.
  [limi]

- Removed superfluous page refresh for IE6 disappearing text bug
  [limi]

- Renamed all JS files to .js instead of js.dtml
  [limi]

- Removed Javascript header declarations
  [limi]

- added .metadata to associate Javascripts with HTTP cache manager
  [limi]

- SiteErrorLog is now created in the Plone site.  This will be easier for
  people to provide us with 'traceback' information.  Before it was created
  at the root of the Zope instance.
  [runyaga]

- **REMOVED** portal_form_validation (which has been deprecated in 1.0) is
  no longer added to your Plone site on construction. the .py file still
  ships with Plone and will be removed in 1.2
  [runyaga]

- Changing your password now requires you enter your current password.
  Also changed the 'change_password' script id to 'plone_change_password'
  to lessen likelihood of clash (we clashed with gruf).  We now override
  MembershipTool.setPassword to call underlying acl_users._doChangeUser
  this way we can pass domain information as well from preferences form.
  [runyaga]

- all the previous migrations have been rolled into 1 migration method
  make_plone and removed ancient cruft (alpha/early betas)
  [runyaga]

- Password generation code now eliminates characters that look alike from
  passwords (e.g. 0 and O, 1 and l, etc).  This should reduce the number of
  user complaints about their initial passwords.
  [geoffd]

- Cookie testing now works for IE 5.0.
  [geoffd]

- Added ExternalEditor as an action in the documentActions area.
  [limi]

- Added support for defining your own default pages in any
  folder. Implemented via browserDefault. The way it works is:

  * if there's a property 'default_page' (must be lines) on
    the folder will use that (normal acquisition applies)

  * if not found, use site_properties

  * if not found, use index_html

  * if not found, use default action
    [andym] [sidnei] [limi] [philikon]

- Added support for FrontPage as a default page in a folder via
  browserDefault.
  This is added to support ZWiki and other Wiki implementations.
  [limi]

- The Presentation/Slide CSS is now optimized for 1024x768,
  which is the most common projector resolution. Too bad
  it's not possible to specify font size relative to the
  screen size.
  [limi]

- Added new Plone Powered icon and a few RSS ones. I don't
  know who the original author of the Powered button is,
  but thanks! :)
  [limi]

- Removed CustomizationPolicy pulldown from ZMI. You can
  still enable it by uncommenting the code if you are
  developing CustomizationPolicies.
  [limi]

- There is a new version of portal_factory in 1.1.
  It lets you create objects which, if you don't save them,
  don't get created in the ZODB. If you want a type to be
  created with portal_factory, add the object's type
  to site_properties/portal_factory_types, and then all
  calls to createObject will use portal_factory.
  [geoffd]

- Removed the CMFWeblog templates and put them in the CMFWeblog
  product instead. Located in the Collective.
  [limi]

- Migration Tool overhaul

  - trimmed down plone initialize

  - added separate setup widgets for languages, skins etc

  - added needUpdating and needRecataloguing

  - added visual notification in the ZMI that the instance
    is out of date

  - added improved log results

  - other improvements
    [andym]

- Added Plone trashcan on behalf of Maik Jablonski
  [andym]

- Fixed Plone Print style sheet - finally prints well in all browsers
  that know how to do printing. Which unfortunately excludes Mozilla
  in its current state. IE and Opera print perfectly, Mozilla prints
  *way* too big.
  [limi]

- Added current time to the standard error message. Useful when your
  users report errors and you want to locate the incident in the
  error logs.
  [limi]

- User Management Screens were added:

  - Users overview - prefs_users_overview - batch user maintenance

  - User details - prefs_user_details - editing attributes of a member

  - User Memberships - prefs_user_memberships - add/remove group
    membership for a user

  - Groups overview - prefs_groups_overview - batch group maintenance

  - Group details - prefs_group_details - editing settings for a group

  - Group Members - prefs_group_members - add/remove members of a group

  - User/Group selection form - prefs_user_group_search_form - a screen
    to select users/groups and feed them back to the other screens

  [limi] [runyaga]

  Note: **Requires**
  "GroupUserFolder from Collective":http://sf.net/projects/collective

- PloneTool.editMetadata made a really bad assumption.  We now use
  interface packages to assert that a object implements the interfaces
  before attempting to set DublinCore attributes *or* Discussable
  attributes.
  [runyaga]

- Now require CMFActionIcons Product from cvs.zope.org.  We register
  document_action icons for such actions as: Send to friend, Print
  this page, and RSS.  Please use the putils (in global_defines.pt)
  getIconFor which will return the id of the icon.
  [runyaga]

- Groups support via GRUF
  [runyaga]

- Removed the Filter pulldown. It doesn't work well, and is not the way to
  cope with the problem of many objects anyway.
  [limi]

- Made it possible to use quoted variable contents in the font selection.
  [limi]

- removed all use of getAuthenticatedMember() in templates -
  now references global 'member' variable:
  'plone_templates/global_defines.pt'
  [runyaga]

- Doesn't show id's if they are autogenerated anymore - context.show_id()
  [runyaga]

- Got rid of getAuthenticatedMember which is deprecated. In main_template
  there is a member variable which does this only once.
  [runyaga]

- Added news slot and event slot to the default slots when a new Plone site
  is created.
  [limi]

- Changed "Welcome" tab to "Home" to be more consistent.
  [limi]

- Changed the events slot, so it shows events that are currently in
  progress. Earlier it didn't display the event when it
  had reached the start date.
  [limi]

- Moved contentEdit before edit (so when you call edit the file knows
  what its new id is)
  [runyaga]

- You can now edit Files from within Plone if they are text/* MIME type.
  [runyaga]

- Several updates to conform to WAI-A and Section 508 accessibility
  guidelines. [sh1mmer]

- Major template clean-up:

    - Separated the global defines into own template
      [limi] [elvix]

    - Separated 'base' calculation into own method, removed slot
      [limi] [elvix]

    - Added global DOCTYPE declaration. This means that no templates should
      have its own declaration.
      [limi] [elvix]

    - Removed all references to the base slot from existing templates, they
      were all just using it to set the noborder variable anyway.
      [limi] [elvix]

    - Refactored main_template **heavily**, it contains no logic anymore,
      only structure.
      [limi] [elvix]

    - Moved all the different parts into scripts or templates outside
      main_template
      [limi] [elvix]

    - Generic cleanup of a lot of bad templates
      [limi] [elvix]

- Added link rel tags for better accessibility, Plone now outputs rel links
  for:

    - Home

    - Contents

    - Search

    - Help

    - Copyright

    - Author

  [limi]

- Plone doesn't use *any* tables for layout anymore. And it works perfectly
  in Netscape 4 too. Amazing, but true ;)
  (Tested in IE, Moz, Opera and NS4, needs Mac IE testing)
  [limi] [elvix]

- Major refactoring of the main_template, it's now squeaky clean.
  [limi] [elvix]

- Lots of cleaning done in the CSS.
  [limi] [elvix]

- DOCTYPE is correctly positioned
  [limi] [elvix]

- All templates have been correctly formatted with regard to this.
  IMPORTANT: All templates should start with an html tag on the first
  line, if you don't put it on the first line, the DOCTYPE will not
  be on the very first line, as Zope renders whitespace before filling
  a slot.
  [limi] [elvix]

- Added 'document_actions' category in portal_actions [runyaga]

- Added check on advanced search form, it now shows a pulldown for authors
  if there are less than 30, and a text input field if there are more.
  [limi]

- The search results page now has a link to the advanced search page.
  Search tab removed when generating new site.
  [limi]

- Content now gets an effective date of "now" if it doesn't have one on a
  state change. Also news now get sorted by effective date. Fixes #1051.
  http://dev.plone.org/plone/ticket/1051
  [ronnix]

- Removed the About slot from site generation. This is not in migrations, as
  it's bad form to mess with people's existing slots - however, new sites
  created with 1.1 should not have it, sinc it is now integrated into the
  documents themselves. [limi]

- removed all .properties files and made them .metadata files
  tal:define="context/rejectAnonymous" and made [ 'security' ] assertions in
  .metadata    [runyaga]

- there is now a folder in the root of the Plone site called 'help' which is
  bootstrapped with 'Document' objects located in CMFPlone/docs. Thus, we
  have inline docs now. [runyaga] [limi]

- ownership_form now reindexes objects when they change ownership. This
  exposes a ugly bug in CMF where Creator=Owner *sigh* [runyaga]

- Made the default content for a homepage called homePageText (was
  originally a PythonScript - sidnei) a PageTemplate.  The biggest problem
  is the first time throw creating an account wrapUser() is called and you
  get a Memberarea created (and your member object has not has
  setMemberProperties called yet) so you dont have access to the
  member properties ;-( [runyaga]

- IDs are now generated using a FSPythonScript, generateUniqueId [runyaga]

- We now require BTreeFolder2, created a 'Large Plone Folder'
  If you have a folder, such as Members who has over a few hundred items
  you should consider using a 'Large Plone Folder'. [runyaga]

- Fixed permissions on PloneFolder methods set in CopySupport.py (1195)
  [runyaga]

- Fixed behaviour of the definition list and pre tags in presentation
  mode. [limi]

- made discussion item preview on the same page using vcXMLRPC, would like
  to do for all content types [andym]

- tabindex can now be used in left/right_slot too. [magnus]

- Breadcrumbs and form validation error messages are now translated [magnus]

- Moved folder_listing into plone_templates [limi]

- New layout for folder_listing, just lists the items with description now,
  is better as a default view [limi]

- Moved the "create default document" to the management side
  (folder_contents) where it belongs [limi]

- CMF from HEAD has version 'Unreleased'. Registered a
  Configuration for it while the apb-redux branch lands. [runyaga]

- Instance version was set to 1.0beta2 on Portal.py

- Removed "(No Description)" string from news.pt

- creates an object to hold customization policy output, if any.

- Added translation to field 'type' in folder_listing table. Replaced
  'n/a' with '&nbsp' to work like folder_contents

- Only show "Add Comment" button if discussion is allowed, and user
  has permission to reply to item.

- integrated browser_default, the default_page variable can be set in site
  properties
  and can be a list of pages to look up in order to find the default:
  eg index.html, index.htm, index_html

- added migration to future to add in default_page

- changed meta_type for portal to be 'Plone Site'

- content_status_history (state tab) form now displays
  the current state in the state list.  This is a usability
  decision. All options should have a default state. Now
  the default is a NOOP, but will not error.  Exposed
  WorkflowException to PythonScripts.

- folder_contents will show lock if portal_lock isLockedOut returns True
  also removed unnecessary traversal

- moved the navigation_tree_builder.py into StatelessTree.py; not sure
  if profiling is correct (or I am reading it) but it said its faster.
  the navigation_tree_slot now uses plone_utils.createNavigationTreeBuilder

- moved documentActions ('print this page', 'send to friend') into a slot
  called item_action_slots which is a proper slot.  Also added a syndication
  widget and all of these are held in plone_templates/ui_slots/actions_slot.pt

- imported nested_scopes in Portal.py and made pre-beta migrations possible

- main_template and header cleanup (needs to be re-aligned with CMFDefault)

- added CMFDefault variables to main_template.pt and moving to use a lot of
  the variables declared in main_template else where in PageTemplates

- items listed in folder_contents generated urls pointing to immediate_view
  (type information)

- not addable portal types are returned by the getNotAddableTypes
  script which can be customized to filter out types based on user
  or context. [philikon]


1.0.5 - Breakbeat Era - Released September 9, 2003
--------------------------------------------------

- Security fix in CMF made us issue a new release with the updated CMF 1.3.2.

- Workaround for the disappearing text bug in Internet Explorer 6 on Windows.


1.0.4 - Zita Swoon - Released August 14, 2003
---------------------------------------------

- Plone is now compliant with the two most widely-used accessibility
  standards in the world - Level A Conformance to the W3C's Web
  Content Accessibility Guidelines (WAI-A) and US Government
  Section 508 compliant.  The law applies to all US Federal agencies
  when they develop, procure, maintain, or use electronic and
  information technology. Under Section 508 (29 U.S.C.  794d),
  agencies must give disabled employees and members of the public
  access to information that is comparable to the access available
  to others. Plone is now able to be used in these agencies.
  [sh1mmer] [limi]

- Removed code that appeared to be causing login problems with IE 5.0.
  To enable testing to see if cookies are enabled when a user logs in,
  you will need to set the property 'test_cookie_name' to some non-empty
  string in portal_properties/site_properties and make sure that your
  main_template actually sets a cookie with the name you have specified.
  See the standard main_template for some sample code.
  [geoffd]

- Backported Print CSS fixes from HEAD. All browsers now print properly,
  apart from Mozilla, which still has some way to go before it understands
  print CSS properly, it seems. Tested in IE and Opera 7.
  [limi]

- PloneFolder.contentValues has grown two args: sort_on and reverse.
  sort_on is a attribute or a callable method on the objects.
  reverse is 0 by default
  [runyaga]


1.0.3 - Brazil - Released June 19, 2003
---------------------------------------

- Fixed ERRATA in 1.0.2

- various bug fixes such as favorites_slot, discussion edit problems

- WorkflowTool.doActionFor was not returning objects if they were moved

- DTML support is now working again (NOTE: deprecated in Plone 1.1)

- added a property in portal_properties/site_properties called invalid_ids
  which will not be allowed to be used in the CMF/Plone site.


1.0.2 - Vert - Released June 3, 2003
------------------------------------

- Fixed permissions on PloneFolder methods set in CopySupport.py (1195)

- 'local roles' tab is now determined by 'Change Permissions' permission.

- If you dont have access to a object you no longer get a login_form but
  a "permission denied" view [gdavis]

- added vcXMLRPC lib

- Fixed behaviour of the definition list and pre tags in presentation
  mode. [limi]

- tabindex can now be used in left/right_slot too.

- Breadcrumbs and form validation error messages are now translated

- Added javascript to warn people that they have cookies disabled before
  they try to log in.

- Added a page that walks people through the process of enabling cookies.

- Fixed up the code that sends users on to their destination when they log
  in.

- When you are logged in and visit a page for which you don't have
  sufficient privileges, you now get a message that says "you have
  insufficient privileges to view this page" rather than a login
  prompt.

- Removed "(No Description)" string in news.pt

- creates an object to hold customization policy results, if any.

- The IE6 fix for invisible text was broken, should work now.

- Added translation to field 'type' in folder_listing table. Replaced
  'n/a' with '&nbsp' to work like folder_contents

- Only show "Add Comment" button if discussion is allowed, and user
  has permission to reply to item.

- added on-error for search results when path('context/%s'%result.getIcon)
  raises a AttributeError

- making less assumptions in Portal/Customization Policy for migrations of
  very old Plones and imported nested_scopes in Portal.py

- visual tidy up of main_template and header and try to see if variables
  have been declared before blindly re-initing them.

- removed the setHeader() in header


1.0.1 - Mira Calix - Released February 19, 2003
-----------------------------------------------

- Added "Dry run" option to portal_migration

- Syndication is now using portal_form.

- calendarDatePickerBox used tabindex instead of tabindex/next

- validation of expiration_date and effective_date in content_status_history was broken

- checkPermission was being traversed to in breadcrumbs, navigation*, and
  my_worklist.

- file/image_edit_form had unexpected behavior.  If you had uploaded
  content (without a Name) it would generate the name.  But if you uploaded
  new content it would rename the object to the new id ;'(.  Thanks to
  Robert Rotterdam for pointing it out and to Limi for having patience ;-).
  we now check isIDAutoGenerated() and if not then we keep the old id.

- added member and portal global variables in main_template for backwards
  compatibility

- fixed bug in new issue formPlone 1.0


1.0 - Released February 6, 2003
-------------------------------

- calendar_slot now uses absolute_url() and template.getId() (so you can stay on templates)

- modified condition of 'state' action in portal_actions so that DTML objects work

- Removed old Xopus files

- Removed XSDHTML editor, all editors should be add-ons and not in core
  Plone

- Added more flexibility for add-on editors by moving format selector into
  wysiwyg_support.pt

- Netscape 4 support is back.

- Fixed IE6's bad handling of floating elements - no more invisible text
  on the pages that triggered this bug. This is done with a couple of lines
  in Javascript - no HTML changes.

- fixed the content_status_modify.failure navigation to goto
  content_status_history instead of old action:publishing thanks to Robert
  Rotterman. NOTE: please do not submit bugs to sourceforge tracker.


1.0 rc2
-------

- removed the properties in site_properties that belong in the root
  validate_email, email_from_name/addr

- added geoff davis's tidy_up.py and tidied up most PageTemplates

- Issue 787 submitted by Ronnix. Fixes the appropriate place of
  email_from_address

- now on a portal_workflow.doActionFor() we reindexObjectSecurity()! I think
  this is already done since we are using DCWorkflow! Specifically this was
  addressed by vlado Issue #442. When a folder has changed its permissions
  and should affect the security for its children.
  http://dev.plone.org/plone/ticket/442

- migration machinery to add skins, change personalize_form to go back to
  personalize_form

- typo in portal_navigation default.folder_rename_form.success should be
  script:folder_rename this typo was propagated throughout previous
  migration scripts and was also fixed. thanks to flacoste for pointing
  this out.

- Rewrote the box code, thanks to interra for help with troubleshooting
  browser bugs. Any customized boxes will need a small update, essentially
  you need to do the following to make a box::

    <div class="box">
      <h5>Title</h5>
      <div class="body">
       Then it's just the usual:
       <div class="even content">

  etc.
  (Remember that you will need to do a Ctrl-F5 (force refresh) to make use
  of the new CSS file - normally it is cached for a day or two)

- Added skin variable to end of CSS file name, avoids caching problems when
  switching skins on the fly.

- Added several new skins. Plone now contains the skins:

    - Plone Autumn

    - Plone Core

    - Plone Core Inverted

    - Plone Corporate

    - Plone Default

    - Plone Greensleeves

    - Plone Kitty

    - Plone Mozilla

    - Plone Mozilla New

    - Plone Prime

    - Plone Zed

- Fix for the printing problems which caused some text to disappear along the
  right edge.

- Added more i18n stuff, the calendar is now fully localized.
  **Remember that you need to run Zope without any special language
  settings for this to work**

- Search results now use the defined time format

- Added CSS workaround for STX tables, they now look like real
  Plone Tables(tm ;)

- Lots and lots of i18n updates


1.0 rc1
-------

- added 'fullname' to portal_memberdata

- 'properties' forms (metadata_edit_form) no longer allows anyone to add keywords.  this is now
  controlled in portal_properties/site_properties/allowRolesToAddKeywords

- Added code to ensure that content object ids do not collide with skin names or reserved ids.

- Added protocol parameter to portal_form_url script.  Fixes issue 593

- Made sure that the main portal types (file, image, document, event, link, newsitem, folder) all
  work with portal_factory.  Cleaned up some minor edit form bugs and added some form titles where
  they were missing.

- Fixed a bug in which uploading two files with the same name in the same folder caused an id
  collision and dumped you into the ZMI.

- Made ids optional for the main portal types (file, image, document, event, link, newsitem, folder).
  If no id is specified, uses the object's current id.  Fixes issue 66.

- Per the request of our usability guru, for items that can have their id set from a file name
  (file, image, document) we show a blank id when the item is first created.

- add_ext_editor script was added.  If you have ExternalEditor installed and
  you run this script; it should configure your system to use it.

- tiny feature.. the filename will remain if your validation fails (not in IE)
  Issue 597

- folder_publish now applied effective/expiration dates and will do so recursively.
  Fixes Issue 605.

- Added site_properties into beta2-beta3 migration script. Thanks interra Issue #659

- Added some navigation properties into the beta2-beta3 migration script that were missing.
  Also put them into the newly created beta3-rc1 migration script for people who migrated
  using the existing script.  Fixes Issue 600.

- Added a fallback for createObject navigation when the new object has no 'edit' action.
  Fixes problems with installing CMFWiki and possibly other packages.

- refactored (only slightly) folder_contents.  Think I may have solved some leakage.
  In previous versions we got a reference to allowedContentTypes and then did a .sort()
  and it seemed ZPT was not cleaning up after itself. ;'( introduced sortObjects (was
  sortObjectValues) and I think its "Doing The Right Thing"

- added lock icon to folder_contents (which automatically will show up in content_status_history)
  and about_slot

- minor optimizations of folder_contents and folder_listing.
  lookup references to objects and then use them instead of repeating lookups.  its pretty
  obvious looking at the table tag what has been defined before being used.  Just Good Practice(tm)


1.0 beta3
---------

- Added all missing i18n strings, merged some strings to better facilitate translations to
  Japanese, Chinese and Korean.

- Renamed Plone XP skin to Plone Corporate to avoid confusion with a certain operating system ;)
  This will break your skinpath if you have it pointing to plone_styles/winxp, change it to
  plone_styles/corporate instead.

- Workflow modification so that Owners can see folder_buttons in Folders that they own.
  Also moved over hardcoded Permissions to constants found in CMFCore.CMFCorePermissions
  fixes Issue 557

- misspell in PloneWorkflow.py found by dc0e - thanks! fixes Issue 579

- the Portal object needs to be 'publicized'.  fixes Issue 569

- if form validation fails for content_status_history keep dates and comments

- since CMFCalendar/Event.py uses a different set of Permissions, 'Change portal events'
  we need to add this permission to the Workflow definitions and set the permissions
  appropriately. fixes Issue 575

- removed a useless conditional check on search_form.pt thanks sspickle!

- Xopus technology preview has been checked in.  It only works on document_edit_forms currently.
  Thanks to q42.nl for the revolutionary technology.  http://xopus.org/
  !!WARNING!!: Careful if you use Mozilla, it swallows the first paragraph when you save at
  the moment. Will be fixed in a later release, this is just to get a feel of how things will
  work.

- turned on the 'SuppressHiddenFiles' in folder_contents and folder_listing.
  Now folders that begin with a . will not show up.  Ideally we would want this turned
  off if we were a Manager.  This is something people can customize themself.
  .personal should be for: Portrait, Personal Events, etc.

- added getFolderContents which wraps listFolderContents for backwards compatibility
  with PortalFolder.  Since it does not provide a suppressHiddenFiles arg we will
  manually apply the suppression in the script.
  navtree_builder has been modified as well so that we will not show these in the navigation tree

- added verifyPermission argument in MembershipTool.py according to Issue 551 thanks to mitja

- in PrivatePlonePolicy made Members folder 'published' so that navigation slot works for Members
  I believe this resolves Issue 489

*NOTE*
We released a beta3 tarball and then decided to fix the above before a final beta3 tarball release


- whether or not /folder_contents is appended to the url in folder_contents is now determined by site_properties/use_folder_contents

- Issue #458 - portal_properties.site_properties is where all Plone/site-wide configuration data is now held

- Moved changes from 1.2 to Portal.py to the migration

- Added the migration tool

- Added PloneInitialize which loads up the ZODB with a Plone instance and some goodies, if and only if the write type of config file that the installer writes is found.

- CustomizationPolicy made the 'folder contents' tab on object un-visible.
  Also changed the name of 'folder contents' for folder category to 'contents'
  Changes 'Publishing' tab title to 'Workflow'

- Added "Print this page" option.

- Reworked the CSS for forms. Should look good in all browsers now, and the
  wrapping problem should be resolved.

- Made all fonts use percentage values, untangled nesting, made textareas use
  non-proportional fonts. Fixed several other visual bugs.

- NavigationExceptions now dump stack traces to the event log rather than including
  them in the error message.

- Object IDs are checked for collision with skin files when renaming objects.  This
  prevents a stack overflow in BSD.

- createObject now uses portal navigation (default is action:edit)

- Added getId and meta_type to the catalog metadata

- Added support for CMFBTreeFolder if it is installed.

- Added a script, portal_form_url.py, that adds portal_form to a URL in the appropriate
  spot.  If you set your form's action to python:context.portal_form_url(template.id), the
  portal_form machinery will kick in upon submission even if the form's URL doesn't have
  portal_form in it initially.

- Added validation for folder_rename and changed the navigation properties accordingly.

- Added "New items since last login" to the logged_in page.

- You can now set the length of the authorization cookie in portal_properties.site_properties

- Added portal_properties.site_properties property sheet for portal wide properties

- Issue 478, folder contents 'add new item' list is now sorted in alphabetical order

- If a member has defined a portrait it will now show up in 'local roles' form
  also the defaultUser.gif portrait will show up in your preferences unless you
  personalize the portrait

- Major CSS update:

- added new box class

- rewrote all boxes (everything in ui_slots)  to use the new code

- made News use the new code

- made Collector use the new code

- made viewThreadsAtBottom use the new code

- moved viewThreadsAtBottom to templates dir

- IMPORTANT: if you have customized your stylesheet properties, you need to add the
  new destructiveButton properties to yours, have a look in stylesheet_properties.props

- All CSS2 style sheets are now contained in plone.css. This causes fewer requests, and a general
  speedup both in rendering and transfer.

- Changed the person icon and name in personal bar to link to page of self, not folder_contents.
  This is more consistent with the use of the person icon elsewhere, and you now have both view
  and folder contents link in personal bar.

- All Netscape4 style sheets were collapsed into on, and re-built. Plone is *much* faster and looks
  much better in Netscape 4.x now.

- fixed ISSUES: 327, 363, 445 (thanks interra!), 485, 60, 491, 495, 364 (CustomizationPolicy), 494,
  488 (more logic in showEditableBorder *sigh*), 452 (gdavis), 349, 437 (Private Policy, thanks
  mitja!), 471 (thanks SDuncan)

- Issue 473 - we now have a standard_error_message python script that
  calls the default_error_message PageTemplate.  Its possible for you to customize this script
  and dispatch to an appropriate PageTemplate depending on the error that was raised.  Thanks
  to Tino Wildenhain for providing insight.  #zope is such a great resource.

- factored out logged_in.pt into 4 entities: logged_in.py (dispatches to appropriate view),
  login_success.pt, login_failed.pt, login_password.pt

- fixed workflow permissions so that:
  if the Manager 'publishes' the root Folder object (so that Members can 'List folder contents')
  that Members can still 'List folder contents' and get the folder_buttons (portal_actions)
  displayed in their home folder.
  NOTE: at the end of CustomizationPolicies both catalog and workflow tool will be 'reindexed'

- file_view uses a href now instead of a input button


1.0 Beta 2
----------

- navigation slot/tree was made more resilient to exceptions thrown while traversing child nodes

- migration script has been updated to transfer portal_memberdata over in a more sane way

- if you only have 1 item you can add dont show drop down list in folder_contents
  just show 'Add New $contenttype' and insert a hidden form variable

- PrivateCustomizationPolicy had *no way* to let anonymous users view content.  This is
  debatable feature but 99% end users will want a transition that allows content to
  be visible by a Anonymous user.  Thus introduced the public state and publicize transition

- PloneFolder mixes in DefaultDublinCoreImpl and declares the DublinCore interface
  also it maps manage_addFolder to manage_addPloneFolder

- By default only Subject keywords assigned in the portal_metadata show up in metadata_edit_form
  instead of the default CMF policy of all Keywords ever assigned + the allowed ones. Also
  alphabetized Keywords and Languages.  Also removed 'None' from dates.

- reconfig_form didn't use the postback value of default language, if the form had errors.

- Bugs fixed 373, 383, 316, 433, 329, 441

- metadate_edit_form added a '\n' in Contributors field, every time it was saved.

- Issue 403 - added '<meta>' tags to header, not really used by modern search engines
  need script listMetaTags.py

- reintroduced getPersonalFolder/getPersonalPortrait python scripts for backwards compatibility

- Topics use folder_workflow now

- added titles for `*_edit_forms` (breadcrumbs seemingly have changed)

- Issue 300 - Standardized batch navigation. Batching now uses PloneBatch and its macro.

- Issue 440 - Forms automatically focus on input element with tabindex=1

- main_template now uses prepare_slots.py

- added structure context/title_or_id to plone_contents and other views.
  Thanks to 'DZ' on plone.org for noticing

- dont show a select box, "Show all items" in folder_contents unless there are types

- gave Manager 'Modify portal content' permission in folder_workflow.published

- closed out Issue 457.  now ppl can define a ploneCustom.css and it will be included in the header

- zwork and limi have worked out quite a few issues regarding the new tree maker


1.0 Beta 1
----------

- Added tree navigation from Philipp Auersperg and made it the default
  navigation device. Thanks!

- Fixed #245, there can now be more than one sortable table on a page.
  Use class listing to make it sortable, class nosort to avoid sorting.

- CustomizationPolicy was not saving changes to personal_form/addtofavorites
  in new_actions now things work as Expected

- moved getPersonalFolder/getPersonalPortrait to portal_membership tool
  instead of FSPythonScripts

- Cleaned out all old javascript, consolidated everything into one file,
  this makes the whole thing more caching-friendly. You can also sort
  any table on any page by putting id="sortable" in the table tag.

- Moved all javascript/ECMAscript into the plone_ecmascript folder. This
  will require earlier instances of Plone to have plone_ecmascript added
  to their skinpath. New sites will work fine.

- The *big* i18n branch was merged into main Plone, breaks the existing
  translation files, (none of who are complete at the moment anyway)
  but is much more future-proof. We have this change in as early as
  possible, and it makes everything much easier to manage from here on.
  to have a much better control over i18n in the future.

- subjects(keywords) in metadata tool were being saved with null property..
  automatically relating items

- filtering was broke changed folder_contents had filter_by_Type where
  CMF1.3 now uses filter_by_portal_type   this required changed to
  folder_contents and filterTypes - only 2 lines of code to change ;) -
  thanks Florrent!

- topic has been changed to to make the icon clickable, it now uses title or
  id of the catalog brain

- related box now has '<br />' separating elements and will not show related
  items that dont have a title - thanks kpm!
  added icons, sort by Type and changed up navigationLocal and only shows
  published items - thanks Raphael Volz!

- MembershipTool.changeMemberPortrait() method added and removed from
  personalize_form

- added MIGRATION documentation

- calendar_slot will only search for items with review_state=published

- width/height are correctly being calculated for all icons (limi fixed)

- added validator for content_status_modify and if folder_publish
  is used for mass publishing it will redirect back to folder_contents
  asking for publishing action if none is supplied

- also fixed the mass publishing which was borked.  now we pass around
  the container

- Issue 266 fixed - topic_view now says 'no results found'

- Issue 288 fixed - favorites slot needed '<br />'

- removed CSSImports and inlined @imports into style tal:content="string"

- put Content-Language to use here.Language() or

- portal_properties.default_language

- changed 'My Stuff' to 'My Folder'

- moved edit_forms in with content

- moved event_* into plone_3rdParty/CMFCalendar for consistency

- Issue 204 fixed

- Sigve Tjora fixed the migration machinery - incredible job!
  CMFPlone/Extensions/migration.py
  Ownership is carried over properly and reindexes newsite
  after migration

- portal_status_message is shown when a object is created, type_name has
  been created.

- Ownership form is wired up but is not visible by default

- added quick_undo script, one step undo.  not visible by default

- removed the download tab on File view since we have a button

- fixed Issue 242, if portal_title==context/title_or_id
  (in a pagetemplate) search for template/id in header -
  thanks ronnix for pointing this out.
  We do this by adding properties on the filesystem i.e.
  search.pt.properties to give search the title=Search results

- '<shiver>' added more logic to breadcrumbs so you can see templates i.e.
  search tab will show
  home >> search form - fixes issue 211 '</shiver>'

- content_status_history.pt now uses Effective/Expiration data accessors

- Andy McKay added nested discussions.

- You can now delete discussions (need to put security check)


1.0 alpha4
----------

- publishing now works without javascript. #202

- moved plone_calendar to plone_3rdParty/CMFCalendar (your skinpath will
  need updating if migrate)

- add ownership_form (so you can change ownership)

- Private plone sites now keep their portal_registration tool, resolving #
  243, #250.

- Anonymous users do not have Add portal member permission in private plone
  sites anymore.

- Members folder is no longer cataloged upon reincarnation as a Plone Folder

- formtooltips for anonymous user are defaulted to portal_memberdata setting

- fixed FreeBSD segfault problem in forms caused by IndexIterator inheriting
  from ZTUtils.Iterator

- Issue 236 resolves - verified by Michael Dietrich

- search_form changed to use portal_type instead of Type thanks to Buehlmann
  and JeffK

- moved all content forms to portal_form machinery

- 'editor view' wasn't going to the parent to list folder_contents

- added personazlie_form/reconfig_form to portal_from machinery

- when you changed password it was forwarding rather than redirecting to
  personalize_form and losing the portal_form proxy

- portal_status_messages have been added for all the `validate_*` and
  `*_edit forms`

- news form now has links to Creators homepage

- first cut at a migration script look Extensions/migration.py

- many more changes

- made a second release of alpha4 with input from Jon Lim - thanks!

- FormTool had typo

- removed old CMF skins in portal_skins

- if your object didn't have a title in a topic it wouldn't show the id

- Issue 345 - content_status_modify wasn't using editMetadata and wasn't guaranteed to
  set the effective/expiration date - FIXED.  and minor aethetic cleanups to boot

- since we got rid of 'index_html' as a PageTemplate and its a Document.  there
  was no flexible way to assign left/right columns easily.  so we now can use
  Folder properties, left_slots and right_slots to put the Path expressions to
  the slots.  These properties are acquired but Membes.right_slots is empty.


1.0 alpha3
----------

- removed tabs, request.set('disable_border',1) from: news, roster, search,
  and search_form

- reconfig_form for site wide configuration has form validation, and exposes
  loads of configuration options

- change in main_template for portal_types to get object_tabs from
  folder/object has been pushed into a property on portal

- added 'use_folder_tabs' property on portal object.  portal_type ids that
  are listed will get folder_actions instead of
  object_actions in main_template.

- fixed edit_topicCriteria (has debug code in it) added navprops entry and
  modified script to use getNextRequestFor

- Members now have default Title/Description Issue 206

- if Casey's incredible ExternalEditor application is installed in ZOPE the
  CustomizationPolicy will integrate it into Plone
  this is the ext_editor boolean property on the Portal Object

- portal_factory tool has been added - Geoff Davis (freakin brilliant)
  this exists to smooth over the fact that you can have empty orphaned
  objects if someone leaves after they
  create a object but before they 'save' changes.  this tool will create a
  proxy object that does not exist
  in the ZODB and the form will be rendered against this proxy object.

- portal_form tool has been added - Geoff Davis (what a great idea!)
  this coordinates the instance, portal_navigation and the edit forms and
  acts like a 'Controller'

- portal_properties has been extended to now be a container - Alan and Geoff
  Davis

- tabindex is now being used to generate the tabindex numbers for all fields

- thanks to Helge!!

- Topic interface has been completely skinned - cheers to Helge/Alex duo!

- if event data isn't set it now shows back up in the form - helge

- integrated XSDHTMLEditor and a way to add other "popup" editor boxes

- publishing tab will not show up for anonymous #224

- added more options in 'plone setup' form

- new Portal wide Property, 'use_folder_tabs' needs to know what Types are
  considered 'Folders' so it shows
  folder tabs and not object tabs.  Wiki/Collector are examples of folderish
  objects that we dont want to see
  folder tabs for.

- Issues resolves: 206, 214, 173, 229, 106, 180 (removed CANCEL for now),
  198, 233 and others

- 'select all' column has been added to folder_contents and general
  folder_contents refactoring

- you can now specify a Default Language for the Portal


1.0alpha2
---------

- Added localLongTimeFormat, set to '%Y-%m-%d %I:%M %p' by default. Used by
  Events.

- Publish tabs now appear on all content types if they have available
  transitions

- configurable tabs and buttons have change:

- local_buttons (in folder_contents form) is now folder_buttons

- local_tabs (on all pages that showborder) are now object_tabs

- global_tabs (at the top of the page) are now portal_tabs

- change status ('mass publishing') now works as expected

- personalize_form was resetting values on form validation failure

- on the rename form you can now change the id and title (maybe the id
  should be optional)

- the way forms interacted with editing scripts has changed:

- form validation has been refactored (basically the only thing you need
  in validate_*.py)

- the actual editing scripts call plone_utils.getNext???For() to get the
  next screen to goto

- look at plone_scripts/form_scripts/navigation_properties.props if you want
  to change this.

- bad id's will not escape the validation machinery

- if you want to disable registration, unregister the registration tool from
  portal_actions and then remove it

- added small IndexIterator utility class (PloneUtilities.IndexIterator), we
  should use this for tabindexs

- metadata_edit_form now has mimetypes/languages boxes that work, also popup
  calendar works now as well

- some python scripts did not have context namespaces bound to them (on the
  filesystem)

- `` __init__.py`` files that declared modules in folders if had 0 bytes made
  winzip unhappy

- folder_contents will no longer show empty dropdown/add new item button or
  (up one level) if they are not usable

- on Plone site creation we now add another workflow definition,
  folder_workflow which is bound to Folder types.

- instead of having a Document as index_html, we use a PageTemplate that
  fills out the master macro and renders
  the CookedBody() of the old index_html, now affectionally called
  'frontpage'

- added a Navigator Controller.  navigational_properties.props is how you
  customize the various page transitions

- everything has been (should be) wired up to the new machinery

- view_source.py has been added to Extensions. use it by
  http://site/object/view_source?template_id=$id

- create external method, id=view_source, module=CMFPlone.view_source,
    function=getObjectSource

- topics have been skinned.  subtopics now share their listing/management of
  subtopics with folder_contents

- removed 'my workspace' (not visible action) until CMFWorkspaces and
  friends land

- undo form now will return you to where you were when you went to the undo
  form

- added a PrivateSiteCustomizationPolicy that makes a plone site "private"
  (preconfigures workflow's) -- you will still need to
  customize the header to get rid of the search_form
  tal:condition="not: context/portal_membership/isAnonymousUser"

- added metadata tab to Event contentType in DefaultCustomizationPolicy

- fixed issue 163

- metadata tab is now labeled Properties

- added XSDHTMLEditor to document form for trial before 1.0


1.0alpha - Boards of Canada Release:
------------------------------------

- refactored how edit scripts work.  lots of heavy lifting is now done in
  plone_utils.editContent()

- specialized WorkflowTool and got rid of sloppy External Methods,
  getWorklists and getAvailableTransitions

- added a Utility object, plone_utils

- tooltips and ID boxes in edit_forms can be turned off in personal settings

- Tres added _cloneActions to ActionProviderBase and co. API  and gave diff
  to CustomizationPolicy. All hail Tres!

- created a CustomizationPolicy for alternate Customizations to be applied
  to Plone on site creation
  these can be separate products that register with the Portal.addPolicy()

- all forms were majorly refactored: popup help boxes were added, i18n
  namespaces were used, general html cleanup

- license changed to GPL, companies can get Plone licensed under BSD - they
  will need to contact Plone Industries

- added transaction notes (exposed on the undo form)

- added form validation to password_form

- renamed recent_news to news

- removed duplicate content_*_forms (publishing forms)

- consolidated the content_status_history and content_publishing_history
  into content_status_history (bad name)
  which can publish 1 object or multiple objects.

- folder_contents now uses actions whose cataegories are local_buttons

- fullname was not being used.  we took it out on personalize form and
  register form (you can add this back)

- metadata_edit_form Discussionabiltiy is now radio boxes not dropdown

- issue #30 - autogenerated passwords only partially being honored

- issue #58 resolved

- issue #52 resolved

- issue #47 resolved

- issue #51 resolved


0.9.9 - Bola - Released May 25, 2002
------------------------------------

- Replaced all references to TextColor with FontColor, added
  headingFontColor property

- New undo page

- New search results page

- All CSS and most HTML validate according to W3C's validators

- fixed up MembershipTool which will add a homepage which will participate
  in workflow

- added a FormulatorTool (portal_form_validation) which is a *thin* wrapper
  around Formulator and exposes
  minimal amounts of functionality.  I didn't know about CMFFormsTool when I
  did this (cmf.zope.org not doing its job)
  so I will have to take another look at whether or not we should go with
  this more advanced component.

- in CSS we have: class="label required" now, and "field error" if a error
  has occurred.

- added validation for all *_edit_forms, look in
  plone_scripts/validate_*

- removed plone_images/img, all images are now in plone_images
    WARNING: you should always specify the full url to the image or caching
    will not occur. ${context/portal_url}/image.gif
    You want to cache as many images on the client side (or in caches in
    front of your ZOPE) as possible.

- navigate* scripts were fixed (thanks to AndyD) which were causing some
  authentication errors

- separated form specific scripts into plone_form_scripts (this includes
  validation scripts)

- file_view when you download no longer puts trailing 0's and uploaded file
  and image views

- file and images will change id's to the uploaded file (strip extension).
  if you -specify- an id, like all other objects the file will be renamed to
  this id regardless of uploaded file
  there is no validation on file and images

- fixed folder_edit (renaming was broke) also added validation - if you
  specify a id, the title is not mandatory.
  we dont want people to have autogenerated ID's in the folder_contents
  listing

- plone_calendar added - thanks to AndyD
    calendar now works out of the box (after running installation script)

- fixed ordinary view and 'up one level'.

- ability to remove MyPortrait

- put absolute paths in for stylehseets (in the @imports we do that in a
  script, CSSImports.py)

- all stylesheets now send back RESPONSE headers that promote caching on
  clients

- in Install/Upgrade we set a property, allowAnonymousViewAbout which
  toggles whether or not anonymous users
  should see a content's about box.  by default it is turned off.
  content_template was impacted

- navigation works nicely if you are logged in. you can 'go up one level'
  to the root URL and then gets it folder_contents
  should promote people to put content in-place.

- join_form is now validated using portal_form_validation, we need people
  to review this code!

- Plone Folder is now the default Folder type inside a portal.

- if there is no index_html defined it will display Directory Listing
      (like Apache)

- folder_listing.pt uses Access Contents Information permission

- if index_html it renders that

- currently old folders are not converted to the Plone Folders in a
      website.  we need to migration script to do this.

- CSS can now be manipulated by CSSValues.py, dont need to customize to the
  CSS themselves. This means you can keep your colors even if we change the
  CSS files.

- individual objects can be toggled discussionable in their metadata edit
  forms (taken from CMF1.2 metadata form)

- discussions attached to a object use structured-text

- from folder_contents you can now publish multiple objects if you have
  permission

- join_box doesn't show up if anonymous doesn't have access to add portal
  member

- Netscape 4.x graceful degrading added. It has its own CSS files.

- review_box shows all content that matches any worklist where you qualify
  NOTE: this means DCWorkflow has now become -required- and you should use
  worklists to assign items to people.

- if you are in multiple worklists, you will not get duplicate entries in
  review list in your UI ;)

- took out unused getObject() calls in search.pt

- Changed ALL pages to use main_template as their template, instead of the
  previous two portal_template and content_template.
  This means we are compatible with all existing CMF Products, although
  they can break our look a bit if they are coded
  badly, which a lot of Products unfortunately are.

- Added new method to deal with CSS values - stylesheet_properties.props

- standard_html_header/footer are now in place for backwards compatibility.
  thanks Evan Simpson!

- Collector and Wiki have been minimally skinned (plone_3rdParty)

- added default content to the root of Plone, index_html

- moved most of the boxes into plone_ui_slots (trying to lighten
  portal_boxes), added FSDirectoryView for ui_slots

- you can now create a Plone site by simply 'Add Plone Site' from inside
  the ZMI (thanks Lalo!)

- suppressed empty comment history in content_status_history

- Calendar slot works as Expected (only published events show up)

- rejected content status no longer redirects to a search page

- if you upload a binary into a Document object, form validation gripes
  [usability issue]

- CMFTopics pretty much work, there is a bit more work to do.

- personalize.py and other CMF1.3 issues have been resolved (setting a
  member properties API has changed in 1.2->1.3)

- showEditableBorder has gone through quite a bit of changes.. still is
  wrong

- Comments have been modified - they are still unusable ;(

- Lucas Marshall pointed out a javascript error in the calendar slot on
  MacOS and a fix 8)

- News items can now use structured-text in the edit_form

- my_worklist works correctly and sorts in ascending order for modified

- you can now edit text of File objects who has text content_type

- added StringIO string access

- added 'change status' button that allows mass publishing of folder
  contents

- refactored filesystem directory view skin structure

- plone_scripts contains scripts and supporting form_scripts

- plone_templates containers site wide templates and supporting ui_slots

- plone_styles container default style and optional plone_themes

- base href is now compatible with how other CMF Products work.  This
  means you can use other CMFProducts out of the box (hopefully ;)

- beginnings of workspace

- moved back to 2 column layout (CMFPlone/Extensions/Upgrade.py
  migrate2ColumnLayout function)

- no longer have to go to folder_factories to create a certain type,
  can do it from folder_contents

- many more changes and cleanups


0.9.8 - Ulrich Schnauss - Released March 19, 2002
-------------------------------------------------

- renaming of objects

- more mozilla enhancements

- calendar support code was optimized (AndyD)

- on Memberarea creation creates a .personal folder for Portrait and
  future private items (by convention)

- fixed it so that http:// isn't always added to link's remote_url

- other things I forgot ;'(


0.9.5 - Released January 31, 2002
---------------------------------

- enormous overhaul of entire UI.  UI now works with Mozilla.
  Install script installs skins
  navigation boxes work (left hand side)

- worked out most deadends

- some security calls have been put in place

- navigation is much nicer and lends itself to more real-world use of CMF as
  filesystem/document sharing

- some cleaning up of code, lots of inefficiencies remaining (
  like listFolderContents)
  breadcrumbs overhauled

- comments have been changed, still more to go before 1.0

- some visual queues exist for users (green border around objects which
  can be edited)

- plone can now be skinned *entirely* using CSS and overriding the /img
  folder
  NOTE: you will need to have copies of all the images in your /img folder

- system should never prompt someone for Username/password if they are
  logged in all `*_edit` scripts return back to objects view

- changing ID works in `*_edit_form`

- you can now customize your 'portrait' in /Members/roster by doing the
  following:

- create a folder, .personal in your home folder

- create a image in .personal called MyPortrait

- publishing your `/Members/*/.personal/MyPortrait` image

- folder_contents now sort (case insensitive) alphabetically by default,
  no more 'pagination' in batches of 10

- added current server time in the top right corner ;)

- content_status_history has been simplified -- still hardcoded
  transitions ;(

- BSD license added (not final license, as will require some non-visual (?)
  attribution)


0.9 - Released January 20th, 2002
---------------------------------

- load of fixes, too many to even attempt to keep track of ;)


0.7 - Released December 12th, 2001
----------------------------------

- folder_edit_form id is editable (not so if its your own member folder id ;)

- new Install.py

- new folder structure (makes more sense)

- new look (content tabs)


0.6
===

- so fast didn't have time to catch 'em


0.5 - Released December 3rd, 2001
---------------------------------

- fixed search form up

- fixed folder_contents (not have an extended_edit, since we muck w/
  metadata a lot)


0.4 - Released October 23rd, 2001
---------------------------------

- Various improvements


0.1 - Released October 4th, 2001
--------------------------------

- Initial release


.. _`commit 2d3865805efc6b72dce236eb68e502d8c57717b6`: https://github.com/plone/Products.CMFPlone/commit/2d3865805efc6b72dce236eb68e502d8c57717b6
.. _`commit bd1f9ba99d1ad40bb7fe1c00eaa32b8884aae5e2`: https://github.com/plone/Products.CMFPlone/commit/bd1f9ba99d1ad40bb7fe1c00eaa32b8884aae5e2
.. _`#78`: https://github.com/plone/Products.CMFPlone/issues/78
.. _`#90`: https://github.com/plone/Products.CMFPlone/issues/90
.. _`#153`: https://github.com/plone/Products.CMFPlone/issues/153
.. _`#163`: https://github.com/plone/Products.CMFPlone/issues/163
.. _`#216`: https://github.com/plone/Products.CMFPlone/issues/216
.. _`#220`: https://github.com/plone/Products.CMFPlone/issues/220
.. _`#290`: https://github.com/plone/Products.CMFPlone/issues/290
.. _`#350`: https://github.com/plone/Products.CMFPlone/issues/350
.. _`#411`: https://github.com/plone/Products.CMFPlone/issues/411
.. _`#454`: https://github.com/plone/Products.CMFPlone/issues/454
.. _`#550`: https://github.com/plone/Products.CMFPlone/issues/550
.. _`#553`: https://github.com/plone/Products.CMFPlone/issues/553
.. _`#557`: https://github.com/plone/Products.CMFPlone/issues/557
.. _`#558`: https://github.com/plone/Products.CMFPlone/issues/558
.. _`#573`: https://github.com/plone/Products.CMFPlone/issues/573
.. _`#604`: https://github.com/plone/Products.CMFPlone/issues/604
.. _`#862`: https://github.com/plone/Products.CMFPlone/issues/862
.. _`#886`: https://github.com/plone/Products.CMFPlone/issues/886
.. _`#895`: https://github.com/plone/Products.CMFPlone/issues/895
.. _`#913`: https://github.com/plone/Products.CMFPlone/issues/913
.. _`#918`: https://github.com/plone/Products.CMFPlone/issues/918
.. _`#926`: https://github.com/plone/Products.CMFPlone/issues/926
.. _`#935`: https://github.com/plone/Products.CMFPlone/issues/935
.. _`#950`: https://github.com/plone/Products.CMFPlone/issues/950
.. _`#952`: https://github.com/plone/Products.CMFPlone/issues/952
.. _`#963`: https://github.com/plone/Products.CMFPlone/issues/963
.. _`#991`: https://github.com/plone/Products.CMFPlone/issues/991
.. _`#996`: https://github.com/plone/Products.CMFPlone/issues/996
.. _`#1015`: https://github.com/plone/Products.CMFPlone/issues/1015
.. _`#1041`: https://github.com/plone/Products.CMFPlone/issues/1041
.. _`#1053`: https://github.com/plone/Products.CMFPlone/issues/1053
.. _`#1232`: https://github.com/plone/Products.CMFPlone/issues/1232
.. _`#1255`: https://github.com/plone/Products.CMFPlone/issues/1255
.. _`#1556`: https://github.com/plone/Products.CMFPlone/issues/1556
