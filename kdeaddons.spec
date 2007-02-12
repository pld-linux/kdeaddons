#
# Conditional build:
%bcond_without  kdegames        # no kdegames dep
%bcond_without	xmms		# no xmms dep
#
%define		_state		unstable
%define		_kdever		3.4.89
%define		_ver		3.4.89
%define         _snap           050629
%define		_minlibsevr	9:3.4.89.050624
%define		_minbaseevr	9:3.4.89.050625

Summary:	K Desktop Environment - Plugins
Summary(es.UTF-8):   K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pl.UTF-8):   Wtyczki do aplikacji KDE
Summary(pt_BR.UTF-8):   K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeaddons
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{_ver}.tar.bz2
Source0:        ftp://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
##% Source0-md5:	596c3a7f4ef43e2f0bd760196a6b119b
BuildRequires:	SDL-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	db-cxx-devel
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= 9:%{_ver}
%{?with_kdegames:BuildRequires:	kdegames-devel >= 8:%{_ver}}
BuildRequires:	kdemultimedia-devel >= 9:%{_ver}
BuildRequires:	kdenetwork-devel >= 10:%{_ver}
BuildRequires:	kdepim-devel >= 3:%{_ver}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	mDNSResponder-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake >= 040511
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for some KDE applications: %{name} extends the functionality
of Konqueror (web browser and file manager), noatun (media player) and
Kate (text editor).

%description -l pl.UTF-8
Wtyczki dla niektórych aplikacji KDE, rozszerzające funkcjonalność
Konquerora (przeglądarki WWW i zarządcy plików), noatun (odtwarzacza
plików multimedialnych), Kate (edytora tekstu).

%description -l pt_BR.UTF-8
kdeaddons contem plugins e scripts adicionais para alguma aplicações
KDE.

%package ark
Summary:	Konqueror ark integration plugin
Summary(pl.UTF-8):   Wtyczka pozwalająca na integrację konquerora z ark
Group:		X11/Applications
Requires:	kdeutils-ark

%description ark
Konqueror plugin for integrating ark (a compression/decompression
program) with the filemanager.

%description ark -l pl.UTF-8
Wtyczka do konquerora integrująca ark (program do
kompresji/dekompresji archiwów) z zarządcą plików.

%package atlantikdesigner
Summary:	Atlantik board designer
Summary(pl.UTF-8):   Program do tworzenia plansz dla gry Atlantik
Group:		X11/Applications/Games
Requires:	kdegames-atlantik >= 8:%{_ver}

%description atlantikdesigner
Atlantik board designer.

%description atlantikdesigner -l pl.UTF-8
Program do tworzenia plansz dla gry Atlantik.

%package fsview
Summary:	FSView - a tool for showing disc utilization in a graphical form
Summary(pl.UTF-8):   FSview - narzędzie do graficznego przedstawiania wolnego miejsca na dysku
Group:		X11/Applications
Requires:	konqueror >= 9:%{_ver}

%description fsview
FSView is a tool for showing disc utilization in a graphical form,
much like the UNIX command 'du'.

%description fsview -l pl.UTF-8
FSview służy do graficznego przedstawiania wolnego miejsca na dysku,
działa podobnie do polecenia 'du'.

%package kaddressbook-plugins
Summary:	Plugins for kaddressbook
Summary(es.UTF-8):   Plugins para kaddressbook
Summary(pl.UTF-8):   Wtyczki do kaddressbook
Summary(pt_BR.UTF-8):   Plugins para kaddressbook
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3:%{_ver}

%description kaddressbook-plugins
Plugins for kaddressbook.

%description kaddressbook-plugins -l es.UTF-8
Este paquete prove plugins de KDE para kaddressbook.

%description kaddressbook-plugins -l pl.UTF-8
Wtyczki do kaddressbook.

%description kaddressbook-plugins -l pt_BR.UTF-8
Este pacote fornece plugins KDE para kaddressbook.

%package kate
Summary:	Plugins for the Kate text editor
Summary(es.UTF-8):   Plugins para kdebase-kate
Summary(pl.UTF-8):   Wtyczki do edytora tekstu Kate
Summary(pt_BR.UTF-8):   Plugins para kdebase-kate
Group:		X11/Applications
Requires:	kdebase-kate >= 9:%{_ver}

%description kate
kdeaddons-kate contains plugins extending the functionality of the
Kate (KDE Advanced Text Editor) editor. kdeaddons-kate adds, among
other things, DCOP support, project management and text filtering
capabilities.

%description kate -l es.UTF-8
Este paquete prove plugins de KDE para kdebase-kate.

%description kate -l pl.UTF-8
Ten pakiet zawiera wtyczki rozszerzające funkcjonalność Kate (KDE
Advanced Text Editor - Zaawansowanego Edytora Tekstów KDE). Dodaje
m.in. obsługę DCOP, możliwość zarządzania projektami i filtrowania
tekstu.

%description kate -l pt_BR.UTF-8
Este pacote fornece plugins KDE para kdebase-kate.

%package kicker
Summary:	Plugins and additional applets for Kicker (the KDE panel)
Summary(es.UTF-8):   Plugins para kdebase-kicker
Summary(pl.UTF-8):   Wtyczki i dodatkowe aplety do Kickera (panelu KDE)
Summary(pt_BR.UTF-8):   Plugins para kdebase-kicker
Group:		X11/Applications
Requires:	kdebase-desktop >= 9:%{_ver}

%description kicker
Plugins and additional applets for Kicker (the KDE panel).

%description kicker -l es.UTF-8
Este paquete prove plugins de KDE para kdebase-kicker.

%description kicker -l pl.UTF-8
Wtyczki i dodatkowe aplety dla Kickera (panelu KDE).

%description kicker -l pt_BR.UTF-8
Este pacote fornece plugins KDE para kdebase-kicker.

%package knewsticker
Summary:	Scripts extending the functionality of KNewsTicker
Summary(pl.UTF-8):   Skrypty rozszerzające funkcjonalność KNewsTickera
Group:		X11/Applications
Requires:	kdenetwork-knewsticker >= 10:%{_ver}

%description knewsticker
Scripts extending the functionality of KNewsTicker.

%description knewsticker -l pl.UTF-8
Skrypty rozszerzające funkcjonalność KNewsTickera.

%package konqueror
Summary:	Plugins extending the functionality of Konqueror
Summary(es.UTF-8):   Plugins para konqueror
Summary(pl.UTF-8):   Wtyczki rozszerzające funkcjonalność Konquerora
Summary(pt_BR.UTF-8):   Plugins para konqueror
Group:		X11/Applications
Requires:	konqueror >= 9:%{_ver}

%description konqueror
Plugins extending the functionality of Konqueror. %{name}-konqueror
contains, among other things, plugins for translating web pages,
checking web pages for valid HTML code, and viewing the DOM tree of
web pages.

%description konqueror -l es.UTF-8
Este paquete prove plugins de KDE para kdebase-konqueror.

%description konqueror -l pl.UTF-8
Pakiet zawiera wtyczki rozszerzające funkcjonalność Konquerora.
Zawiera m.in. wtyczki do tłumaczenia stron WWW, sprawdzania
poprawności HTML-a, oglądania drzewa DOM stron WWW.

%description konqueror -l pt_BR.UTF-8
Este pacote fornece plugins KDE para kdebase-konqueror.

%package ksig
Summary:	A signature creator and manager
Summary(pl.UTF-8):   Program tworzący i zarządzający podpisami
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{_ver}

%description ksig
A signature creator and manager.

%description ksig -l pl.UTF-8
Program tworzący i zarządzający podpisami.

%package kvim
Summary:	Vim KPart
Summary(pl.UTF-8):   KPart z vimem
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{_ver}

%description kvim
A kpart allowing KDE apps to embedd vim as an editor.

%description kvim -l pl.UTF-8
KPart umożliwiający aplikacjom KDE wykorzystywanie vima jako
osadzonego edytora.

%package lnkforward
Summary:	Windows link file forwarder
Summary(pl.UTF-8):   Przekierowywacz skrótów windowsowych
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{_ver}

%description lnkforward
A konqueror extension that makes windows .lnk files work under Linux.

%description lnkforward -l pl.UTF-8
Rozszerzenie do konquerora sprawiające, że windowsowe skróty .lnk
działają pod Linuksem.

%package noatun
Summary:	Plugins extending the functionality of the noatun media player
Summary(es.UTF-8):   Plugins para kdemultimedia-noatun
Summary(pl.UTF-8):   Wtyczki rozszerzające funkcjonalność odtwarzacza noatun
Summary(pt_BR.UTF-8):   Plugins para kdemultimedia-noatun
Group:		X11/Applications
Requires:	kdemultimedia-noatun >= 9:%{_ver}

%description noatun
Plugins extending the functionality of the noatun media player.

%description noatun -l es.UTF-8
Este paquete prove plugins de KDE para kdemultimedia-noatun.

%description noatun -l pl.UTF-8
Wtyczki rozszerzające funkcjonalność odtwarzacza plików
multimedialnych noatun.

%description noatun -l pt_BR.UTF-8
Este pacote fornece plugins KDE para kdemultimedia-noatun.

%prep
#%setup -q
%setup -q -n %{name}-%{_snap}

%build
cp -f /usr/share/automake/config.sub admin

#export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

mv $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color/16x16/apps/autorefresh.png

%find_lang kate-plugins		--with-kde
%find_lang kicker-applets	--with-kde
%find_lang konq-plugins		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	kvim	-p /sbin/ldconfig
%postun	kvim	-p /sbin/ldconfig

%files ark
%defattr(644,root,root,755)
%{_libdir}/kde3/libarkplugin.la
%attr(755,root,root) %{_libdir}/kde3/libarkplugin.so
%{_datadir}/applnk/.hidden/arkplugin.desktop
%{_datadir}/services/ark_plugin.desktop

%if %{with kdegames}
%files atlantikdesigner
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atlantikdesigner
%{_datadir}/apps/atlantikdesigner
%{_desktopdir}/kde/atlantikdesigner.desktop
%{_iconsdir}/*/*/*/atlantikdesigner.png
%{_mandir}/man1/atlantikdesigner.1*
%endif

%files fsview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fsview
%{_libdir}/kde3/libfsviewpart.la
%attr(755,root,root) %{_libdir}/kde3/libfsviewpart.so
%{_datadir}/apps/fsview
%{_datadir}/services/fsview_part.desktop
%{_iconsdir}/*/*/apps/fsview.png
%{_mandir}/man1/fsview.1*

%files kaddressbook-plugins
%defattr(644,root,root,755)
%{_libdir}/kde3/libkaddrbk_geo_xxport.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_geo_xxport.so
%{_libdir}/kde3/libkaddrbk_gmx_xxport.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_gmx_xxport.so
%{_datadir}/apps/kaddressbook/geo_xxportui.rc
%{_datadir}/apps/kaddressbook/gmx_xxportui.rc
%{_datadir}/services/kaddressbook/geo_xxport.desktop
%{_datadir}/services/kaddressbook/gmx_xxport.desktop

%files kate -f kate-plugins.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kate*.la
%attr(755,root,root) %{_libdir}/kde3/kate*.so
%{_libdir}/kde3/libkatetabbarextensionplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkatetabbarextensionplugin.so
%{_datadir}/apps/kate/plugins/*
%{_datadir}/apps/kate/scripts/html-tidy.desktop
%{_datadir}/apps/katepart/syntax/katetemplate.xml
%attr(755,root,root) %{_datadir}/apps/kate/scripts/html-tidy.sh
%{_datadir}/apps/katexmltools
%{_datadir}/services/kate*
%{_datadir}/applnk/.hidden/katefll.desktop

%files kicker -f kicker-applets.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kbinaryclock_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kbinaryclock_panelapplet.so
%{_libdir}/kde3/kolourpicker_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kolourpicker_panelapplet.so
%{_libdir}/kde3/ktimemon_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/ktimemon_panelapplet.so
%{_libdir}/kde3/math_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/math_panelapplet.so
%{_libdir}/kde3/mediacontrol_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/mediacontrol_panelapplet.so
%{_datadir}/apps/kicker/applets/kbinaryclock.desktop
%{_datadir}/apps/kicker/applets/kolourpicker.desktop
%{_datadir}/apps/kicker/applets/ktimemon.desktop
%{_datadir}/apps/kicker/applets/mathapplet.desktop
%{_datadir}/apps/kicker/applets/mediacontrol.desktop
%{_datadir}/apps/mediacontrol
%{_datadir}/config.kcfg/kbinaryclock.kcfg
%{_iconsdir}/crystalsvg/*/apps/ktimemon.png
%{_iconsdir}/hicolor/*/apps/autorefresh.png

%files knewsticker
%defattr(644,root,root,755)
%dir %{_datadir}/apps/knewsticker/scripts
%{_datadir}/apps/knewsticker/scripts/Generic.Newsticker.Error
%{_datadir}/apps/knewsticker/scripts/Readme.ErrorHandling
%{_datadir}/apps/knewsticker/scripts/Readme.newsrss
%{_datadir}/apps/knewsticker/scripts/Readme.stock
%{_datadir}/apps/knewsticker/scripts/bbc.pl
%{_datadir}/apps/knewsticker/scripts/fyensget.py
%{_datadir}/apps/knewsticker/scripts/newsrss.pl
%{_datadir}/apps/knewsticker/scripts/sportscores.py
%{_datadir}/apps/knewsticker/scripts/stock.pl

%files konqueror -f konq-plugins.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exif.py
%attr(755,root,root) %{_bindir}/jpegorient
%attr(755,root,root) %{_bindir}/kio_media_realfolder
%attr(755,root,root) %{_bindir}/orient.py
%{_libdir}/kde3/kfile_cert.la
%attr(755,root,root) %{_libdir}/kde3/kfile_cert.so
%{_libdir}/kde3/kfile_desktop.la
%attr(755,root,root) %{_libdir}/kde3/kfile_desktop.so
%{_libdir}/kde3/kfile_folder.la
%attr(755,root,root) %{_libdir}/kde3/kfile_folder.so
%{_libdir}/kde3/kfile_html.la
%attr(755,root,root) %{_libdir}/kde3/kfile_html.so
%{_libdir}/kde3/kfile_mhtml.la
%attr(755,root,root) %{_libdir}/kde3/kfile_mhtml.so
%{_libdir}/kde3/kfile_txt.la
%attr(755,root,root) %{_libdir}/kde3/kfile_txt.so
%{_libdir}/kde3/konqsidebar_mediaplayer.la
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_mediaplayer.so
%{_libdir}/kde3/libautorefresh.la
%attr(755,root,root) %{_libdir}/kde3/libautorefresh.so
%{_libdir}/kde3/libbabelfishplugin.la
%attr(755,root,root) %{_libdir}/kde3/libbabelfishplugin.so
%{_libdir}/kde3/libcrashesplugin.la
%attr(755,root,root) %{_libdir}/kde3/libcrashesplugin.so
%{_libdir}/kde3/libdirfilterplugin.la
%attr(755,root,root) %{_libdir}/kde3/libdirfilterplugin.so
%{_libdir}/kde3/libdomtreeviewerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libdomtreeviewerplugin.so
%{_libdir}/kde3/libmfkonqmficon.la
%attr(755,root,root) %{_libdir}/kde3/libmfkonqmficon.so
%{_libdir}/kde3/libsearchbarplugin.la
%attr(755,root,root) %{_libdir}/kde3/libsearchbarplugin.so
%{_libdir}/kde3/kcm_kuick.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kuick.so
%{_libdir}/kde3/libkhtmlsettingsplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkhtmlsettingsplugin.so
%{_libdir}/kde3/libkimgallery.la
%attr(755,root,root) %{_libdir}/kde3/libkimgallery.so
%{_libdir}/kde3/libkuickplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkuickplugin.so
%{_libdir}/kde3/libminitoolsplugin.la
%attr(755,root,root) %{_libdir}/kde3/libminitoolsplugin.so
%{_libdir}/kde3/librenaudioplugin.la
%attr(755,root,root) %{_libdir}/kde3/librenaudioplugin.so
%{_libdir}/kde3/librenimageplugin.la
%attr(755,root,root) %{_libdir}/kde3/librenimageplugin.so
%{_libdir}/kde3/libuachangerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libuachangerplugin.so
%{_libdir}/kde3/libvalidatorsplugin.la
%attr(755,root,root) %{_libdir}/kde3/libvalidatorsplugin.so
%{_libdir}/kde3/libwebarchiverplugin.la
%attr(755,root,root) %{_libdir}/kde3/libwebarchiverplugin.so
%{_libdir}/kde3/webarchivethumbnail.la
%attr(755,root,root) %{_libdir}/kde3/webarchivethumbnail.so
%{_datadir}/apps/domtreeviewer
%{_datadir}/apps/khtml/kpartplugins/autorefresh.desktop
%{_datadir}/apps/khtml/kpartplugins/autorefresh.rc
%{_datadir}/apps/khtml/kpartplugins/babelfishplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/crashesplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/crashesplugin.rc
%{_datadir}/apps/khtml/kpartplugins/domtreeviewerplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/mf_konqmficon.desktop
%{_datadir}/apps/khtml/kpartplugins/mf_konqmficon.rc
%{_datadir}/apps/khtml/kpartplugins/minitoolsplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/minitoolsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_babelfish.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_babelfish.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_domtreeviewer.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_domtreeviewer.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_rellinks.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_validators.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_validators.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_webarchiver.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_webarchiver.rc
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.rc
%{_datadir}/apps/khtml/kpartplugins/validatorsplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/webarchiverplugin.desktop
%{_datadir}/apps/konqiconview/kpartplugins/dirfilterplugin.desktop
%{_datadir}/apps/konqiconview/kpartplugins/dirfilterplugin.rc
%{_datadir}/apps/konqiconview/kpartplugins/kimgalleryplugin.desktop
%{_datadir}/apps/konqiconview/kpartplugins/kimgalleryplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/dirfilterplugin.desktop
%{_datadir}/apps/konqlistview/kpartplugins/dirfilterplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/kimgalleryplugin.desktop
%{_datadir}/apps/konqlistview/kpartplugins/kimgalleryplugin.rc
%{_datadir}/apps/konqsidebartng/add/mplayer_add.desktop
%{_datadir}/apps/konqueror/kpartplugins
%{_datadir}/apps/konqueror/servicemenus/imageconverter.desktop
%{_datadir}/apps/konqueror/servicemenus/jpegorient.desktop
%{_datadir}/apps/konqueror/servicemenus/media_realfolder.desktop
%{_datadir}/apps/microformat
%{_datadir}/config/translaterc
%{_datadir}/services/kfile_cert.desktop
%{_datadir}/services/kfile_desktop.desktop
%{_datadir}/services/kfile_folder.desktop
%{_datadir}/services/kfile_html.desktop
%{_datadir}/services/kfile_mhtml.desktop
%{_datadir}/services/kfile_txt.desktop
%{_datadir}/services/kuick_plugin.desktop
%{_datadir}/services/renaudiodlg.desktop
%{_datadir}/services/renimagedlg.desktop
%{_datadir}/services/webarchivethumbnail.desktop
%{_datadir}/applnk/.hidden/kcmkuick.desktop
#%{_datadir}/applnk/.hidden/kimgalleryplugin.desktop
%{_datadir}/applnk/.hidden/kuickplugin.desktop
%{_datadir}/applnk/.hidden/mediaplayerplugin.desktop
%{_iconsdir}/crystalsvg/*/actions/babelfish.png
%{_iconsdir}/crystalsvg/*/actions/cssvalidator.png
%{_iconsdir}/crystalsvg/*/actions/domtreeviewer.png
%{_iconsdir}/crystalsvg/*/actions/htmlvalidator.png
%{_iconsdir}/crystalsvg/*/actions/imagegallery.png
%{_iconsdir}/*/*/actions/minitools.*
%{_iconsdir}/crystalsvg/*/actions/validators.png
%{_iconsdir}/crystalsvg/*/actions/webarchiver.png
%{_iconsdir}/crystalsvg/*/apps/konqsidebar_mediaplayer.png
%{_mandir}/man1/exif.py.1*
%{_mandir}/man1/jpegorient.1*
%{_mandir}/man1/orient.py.1*
# TODO - requires kdenetwork-{knewsticker,rss}
%{_libdir}/kde3/konq_sidebarnews.la
%attr(755,root,root) %{_libdir}/kde3/konq_sidebarnews.so
%{_datadir}/apps/konqsidebartng/add/news_add.desktop
%{_datadir}/apps/konqueror/icons/crystalsvg/16x16/actions/google.png
%{_datadir}/config.kcfg/konq_sidebarnews.kcfg
%{_iconsdir}/crystalsvg/*/apps/konqsidebar_news.png
# TODO - requires kdepim (akregator)
%{_libdir}/kde3/libakregatorkonqfeedicon.la
%attr(755,root,root) %{_libdir}/kde3/libakregatorkonqfeedicon.so
%{_libdir}/kde3/libakregatorkonqplugin.la
%attr(755,root,root) %{_libdir}/kde3/libakregatorkonqplugin.so
%{_datadir}/apps/akregator/pics/rss.png
%{_datadir}/apps/khtml/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/apps/khtml/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/services/akregator_konqplugin.desktop

%files ksig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksig
%{_datadir}/apps/ksig
%{_desktopdir}/kde/ksig.desktop
%{_iconsdir}/*/*/apps/ksig.png
%{_mandir}/man1/ksig.1*

#%files kvim
#%defattr(644,root,root,755)
#%{_libdir}/libxvim.la
#%attr(755,root,root) %{_libdir}/libxvim.so
#%attr(755,root,root) %{_libdir}/libxvim.so.*.*.*
#%{_libdir}/kde3/kcm_vim.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_vim.so
#%{_libdir}/kde3/libvimpart.la
#%attr(755,root,root) %{_libdir}/kde3/libvimpart.so*
#%{_datadir}/apps/kcontrol/pics/kvim.png
#%{_datadir}/apps/vimpart
#%{_datadir}/services/vimpart.desktop
#%{_desktopdir}/kde/kcmvim.desktop

%files lnkforward
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lnkforward
%{_libdir}/kde3/kfile_lnk.la
%attr(755,root,root) %{_libdir}/kde3/kfile_lnk.so
%{_libdir}/kde3/librellinksplugin.la
%attr(755,root,root) %{_libdir}/kde3/librellinksplugin.so
%{_datadir}/applnk/.hidden/lnkforward.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_rellinks.rc
%{_datadir}/mimelnk/application/x-win-lnk.desktop
%{_datadir}/services/kfile_lnk.desktop
%{_mandir}/man1/lnkforward.1*

%files noatun
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatunsynaescope.bin
%attr(755,root,root) %{_bindir}/noatuntippecanoe.bin
%attr(755,root,root) %{_bindir}/noatuntyler.bin
%{_libdir}/kde3/noatun_ffrs.la
%attr(755,root,root) %{_libdir}/kde3/noatun_ffrs.so
%{_libdir}/kde3/noatunalsaplayer.la
%attr(755,root,root) %{_libdir}/kde3/noatunalsaplayer.so
%{_libdir}/kde3/noatunblurscope.la
%attr(755,root,root) %{_libdir}/kde3/noatunblurscope.so
%{_libdir}/kde3/noatuncharlatan.la
%attr(755,root,root) %{_libdir}/kde3/noatuncharlatan.so
%{_libdir}/kde3/noatun_oblique.la
%attr(755,root,root) %{_libdir}/kde3/noatun_oblique.so
%{_libdir}/kde3/noatundub.la
%attr(755,root,root) %{_libdir}/kde3/noatundub.so
%{_libdir}/kde3/noatunluckytag.la
%attr(755,root,root) %{_libdir}/kde3/noatunluckytag.so
%{_libdir}/kde3/noatunlyrics.la
%attr(755,root,root) %{_libdir}/kde3/noatunlyrics.so
%{_libdir}/kde3/noatunmadness.la
%attr(755,root,root) %{_libdir}/kde3/noatunmadness.so
%{_libdir}/kde3/noatunpitchablespeed.la
%attr(755,root,root) %{_libdir}/kde3/noatunpitchablespeed.so
%{_libdir}/kde3/noatunsynaescope.la
%attr(755,root,root) %{_libdir}/kde3/noatunsynaescope.so
%{_libdir}/kde3/noatuntippecanoe.la
%attr(755,root,root) %{_libdir}/kde3/noatuntippecanoe.so
%{_libdir}/kde3/noatuntyler.la
%attr(755,root,root) %{_libdir}/kde3/noatuntyler.so
%{_libdir}/kde3/noatunwakeup.la
%attr(755,root,root) %{_libdir}/kde3/noatunwakeup.so
%{_libdir}/kde3/noatunwavecapture.la
%attr(755,root,root) %{_libdir}/kde3/noatunwavecapture.so
%{_datadir}/apps/noatun/*
%{_iconsdir}/crystalsvg/*/apps/synaescope.png
%{_mandir}/man1/noatunsynaescope.bin.1*
%{_mandir}/man1/noatuntippecanoe.bin.1*
%{_mandir}/man1/noatuntyler.bin.1*
