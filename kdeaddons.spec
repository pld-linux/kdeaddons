%bcond_without  kdegames        # no kdegames dep
%define		_state		stable
%define		_ver		3.3.1


Summary:	K Desktop Environment - Plugins
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pl):	Wtyczki do aplikacji KDE
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplica��es KDE
Name:		kdeaddons
Version:	%{_ver}
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
# Source0-md5:	69ec1deff7ae2d0c3602bb141ed4c546
Patch100:	%{name}-branch.diff
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
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for some KDE applications: %{name} extends the functionality
of Konqueror (web browser and file manager), noatun (media player) and
Kate (text editor).

%description -l pl
Wtyczki dla niekt�rych aplikacji KDE, rozszerzaj�ce funkcjonalno��
Konquerora (przegl�darki WWW i zarz�dcy plik�w), noatun (odtwarzacza
plik�w multimedialnych), Kate (edytora tekstu).

%description -l pt_BR
kdeaddons contem plugins e scripts adicionais para alguma aplica��es
KDE.

%package ark
Summary:	Konqueror ark integration plugin
Summary(pl):	Wtyczka pozwalaj�ca na integracj� konquerora z ark
Group:		X11/Applications
Requires:	kdeutils-ark

%description ark
Konqueror plugin for integrating ark (a compression/decompression
program) with the filemanager.

%description ark -l pl
Wtyczka do konquerora integruj�ca ark (program do
kompresji/dekompresji archiw�w) z mened�erem plik�w.

%package atlantikdesigner
Summary:	Atlantik board designer
Summary(pl):	Program do tworzenia plansz dla gry Atlantik
Group:		X11/Applications/Games
Requires:	kdegames-atlantik >= 8:%{_ver}

%description atlantikdesigner
Atlantik board designer.

%description atlantikdesigner -l pl
Program do tworzenia plansz dla gry Atlantik.

%package fsview
Summary:	FSView - a tool for showing disc utilization in a graphical form
Summary(pl):	FSview - narz�dzie do graficznego przedstawiania wolnego miejsca na dysku
Group:		X11/Applications
Requires:	konqueror >= 9:%{_ver}

%description fsview
FSView is a tool for showing disc utilization in a graphical form,
much like the UNIX command 'du'.

%description fsview -l pl
FSview s�u�y do graficznego przedstawiania wolnego miejsca na dysku,
dzia�a podobnie do polecenia 'du'.

%package kaddressbook-plugins
Summary:	Plugins for kaddressbook
Summary(es):	Plugins para kaddressbook
Summary(pl):	Wtyczki do kaddressbook
Summary(pt_BR):	Plugins para kaddressbook
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3:%{_ver}

%description kaddressbook-plugins
Plugins for kaddressbook.

%description kaddressbook-plugins -l es
Este paquete prove plugins de KDE para kaddressbook.

%description kaddressbook-plugins -l pl
Wtyczki do kaddressbook.

%description kaddressbook-plugins -l pt_BR
Este pacote fornece plugins KDE para kaddressbook.

%package kate
Summary:	Plugins for the Kate text editor
Summary(es):	Plugins para kdebase-kate
Summary(pl):	Wtyczki do edytora tekstu Kate
Summary(pt_BR):	Plugins para kdebase-kate
Group:		X11/Applications
Requires:	kdebase-kate >= 9:%{_ver}

%description kate
kdeaddons-kate contains plugins extending the functionality of the
Kate (KDE Advanced Text Editor) editor. kdeaddons-kate adds, among
other things, DCOP support, project management and text filtering
capabilities.

%description kate -l es
Este paquete prove plugins de KDE para kdebase-kate.

%description kate -l pl
Ten pakiet zawiera wtyczki rozszerzaj�ce funkcjonalno�� Kate (KDE
Advanced Text Editor - Zaawansowanego Edytora Tekst�w KDE). Dodaje
m.in. obs�ug� DCOP, mo�liwo�� zarz�dzania projektami i filtrowania
tekstu.

%description kate -l pt_BR
Este pacote fornece plugins KDE para kdebase-kate.

%package kicker
Summary:	Plugins and additional applets for Kicker (the KDE panel)
Summary(es):	Plugins para kdebase-kicker
Summary(pl):	Wtyczki i dodatkowe aplety do Kickera (panelu KDE)
Summary(pt_BR):	Plugins para kdebase-kicker
Group:		X11/Applications
Requires:	kdebase-desktop >= 9:%{_ver}

%description kicker
Plugins and additional applets for Kicker (the KDE panel).

%description kicker -l es
Este paquete prove plugins de KDE para kdebase-kicker.

%description kicker -l pl
Wtyczki i dodatkowe aplety dla Kickera (panelu KDE).

%description kicker -l pt_BR
Este pacote fornece plugins KDE para kdebase-kicker.

%package knewsticker
Summary:	Scripts extending the functionality of KNewsTicker
Summary(pl):	Skrypty rozszerzaj�ce funkcjonalno�� KNewsTickera
Group:		X11/Applications
Requires:	kdenetwork-knewsticker >= 10:%{_ver}

%description knewsticker
Scripts extending the functionality of KNewsTicker.

%description knewsticker -l pl
Skrypty rozszerzaj�ce funkcjonalno�� KNewsTickera.

%package konqueror
Summary:	Plugins extending the functionality of Konqueror
Summary(es):	Plugins para konqueror
Summary(pl):	Wtyczki rozszerzaj�ce funkcjonalno�� Konquerora
Summary(pt_BR):	Plugins para konqueror
Group:		X11/Applications
Requires:	konqueror >= 9:%{_ver}

%description konqueror
Plugins extending the functionality of Konqueror. %{name}-konqueror
contains, among other things, plugins for translating web pages,
checking web pages for valid HTML code, and viewing the DOM tree of
web pages.

%description konqueror -l es
Este paquete prove plugins de KDE para kdebase-konqueror.

%description konqueror -l pl
Pakiet zawiera wtyczki rozszerzaj�ce funkcjonalno�� Konquerora.
Zawiera m.in. wtyczki do t�umaczenia stron WWW, sprawdzania
poprawno�ci HTML-a, ogl�dania drzewa DOM stron WWW.

%description konqueror -l pt_BR
Este pacote fornece plugins KDE para kdebase-konqueror.

#%package kontact
#Summary:	Plugins extending the functionality of Kontact
#Summary(pl):	Wtyczki rozszerzaj�ce funkcjonalno�� Kontact
#Group:		X11/Applications
#Requires:	kdepim >= 3:%{_ver}
#Requires:	kdenetwork-knewsticker >= 10:%{_ver}
#
#%description kontact
#Plugins extending the functionality of Kontact. This includes an rss
#feeds module.
#
#%description kontact -l pl
#Wtyczki rozszerzaj�ce funkcjonalno�� Kontact. Pakiet zawiera modu�
#wy�wietlaj�cy �r�d�a rss.

%package ksig
Summary:	A signature creator and manager
Summary(pl):	Program tworz�cy i zarz�dzaj�cy podpisami
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{_ver}

%description ksig
A signature creator and manager.

%description ksig -l pl
Program tworz�cy i zarz�dzaj�cy podpisami.

%package kvim
Summary:	Vim KPart
Summary(pl):	KPart z vimem
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{_ver}

%description kvim
A kpart allowing KDE apps to embedd vim as an editor.

%description kvim -l pl
KPart umo�liwiaj�cy aplikacjom KDE wykorzystywanie vima jako
osadzonego edytora.

%package lnkforward
Summary:	Windows link file forwarder
Summary(pl):	Przekierowywacz skr�t�w windowsowych
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{_ver}

%description lnkforward
A konqueror extension that makes windows .lnk files work under linux.

%description lnkforward -l pl
Rozszerzenie do konquerora sprawiaj�ce, �e windowsowe skr�ty .lnk
dzia�aj� pod Linuksem.

%package noatun
Summary:	Plugins extending the functionality of the noatun media player
Summary(es):	Plugins para kdemultimedia-noatun
Summary(pl):	Wtyczki rozszerzaj�ce funkcjonalno�� odtwarzacza noatun
Summary(pt_BR):	Plugins para kdemultimedia-noatun
Group:		X11/Applications
Requires:	kdemultimedia-noatun >= 9:%{_ver}

%description noatun
Plugins extending the functionality of the noatun media player.

%description noatun -l es
Este paquete prove plugins de KDE para kdemultimedia-noatun.

%description noatun -l pl
Wtyczki rozszerzaj�ce funkcjonalno�� odtwarzacza plik�w
multimedialnych noatun.

%description noatun -l pt_BR
Este pacote fornece plugins KDE para kdemultimedia-noatun.

%prep
%setup -q
%patch100 -p1

echo "KDE_OPTIONS = nofinal" >> noatun-plugins/luckytag/Makefile.am

%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	vimpart/kcmvim/kcmvim.desktop
%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	-e 's/Terminal=0/Terminal=false/' \
	atlantikdesigner/atlantikdesigner.desktop
%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	ksig/ksig.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '^Categories=.*[^;]$' $f; then
		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
	fi
done

%build
cp -f %{_datadir}/automake/config.sub admin

export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

export LDFLAGS="%{rpmldflags} -lpthread"

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
#%{_applnkdir}/.hidden/fsview.desktop
#%{_desktopdir}/kde/fsview.desktop
%{_iconsdir}/*/*/apps/fsview.png
%{_mandir}/man1/fsview.1*

%files kaddressbook-plugins
%defattr(644,root,root,755)
%{_libdir}/kde3/libkaddrbk_geo_xxport.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_geo_xxport.so
%{_datadir}/apps/kaddressbook/geo_xxportui.rc
%{_datadir}/services/kaddressbook/geo_xxport.desktop

%files kate -f kate-plugins.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kate*.la
%attr(755,root,root) %{_libdir}/kde3/kate*.so
%{_libdir}/kde3/libkatetabbarextensionplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkatetabbarextensionplugin.so
%{_datadir}/apps/kate/plugins/*
%{_datadir}/apps/kate/scripts/html-tidy.desktop
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
%attr(755,root,root) %{_bindir}/orient.py
%{_libdir}/kde3/kfile_desktop.la
%attr(755,root,root) %{_libdir}/kde3/kfile_desktop.so
%{_libdir}/kde3/kfile_folder.la
%attr(755,root,root) %{_libdir}/kde3/kfile_folder.so
%{_libdir}/kde3/kfile_html.la
%attr(755,root,root) %{_libdir}/kde3/kfile_html.so
%{_libdir}/kde3/kfile_txt.la
%attr(755,root,root) %{_libdir}/kde3/kfile_txt.so
%{_libdir}/kde3/konq_smbmounterplugin.la
%attr(755,root,root) %{_libdir}/kde3/konq_smbmounterplugin.so
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
%{_datadir}/apps/khtml/kpartplugins/autorefresh.rc
%{_datadir}/apps/khtml/kpartplugins/crashesplugin.rc
%{_datadir}/apps/khtml/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/minitoolsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_babelfish.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_domtreeviewer.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_validators.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_webarchiver.rc
# What's up??!!
%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/kpartplugins
%{_datadir}/apps/konqueror/kpartplugins/searchbar.rc
#
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.rc
%{_datadir}/apps/konqiconview/kpartplugins/dirfilterplugin.rc
%{_datadir}/apps/konqiconview/kpartplugins/kimgalleryplugin.rc
%{_datadir}/apps/konqiconview/kpartplugins/smbmounterplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/dirfilterplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/kimgalleryplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/smbmounterplugin.rc
%{_datadir}/apps/konqsidebartng/add/mplayer_add.desktop
#%{_datadir}/apps/konqsidebartng/entries/mplayer.desktop
#%{_datadir}/apps/konqsidebartng/kicker_entries/mplayer.desktop
%{_datadir}/apps/konqueror/servicemenus/imageconverter.desktop
%{_datadir}/apps/konqueror/servicemenus/jpegorient.desktop
%{_datadir}/config/translaterc
%{_datadir}/mimelnk/application/x-webarchive.desktop
%{_datadir}/services/kfile_desktop.desktop
%{_datadir}/services/kfile_folder.desktop
%{_datadir}/services/kfile_html.desktop
%{_datadir}/services/kfile_txt.desktop
%{_datadir}/services/kuick_plugin.desktop
%{_datadir}/services/renaudiodlg.desktop
%{_datadir}/services/renimagedlg.desktop
%{_datadir}/services/webarchivethumbnail.desktop
%{_datadir}/applnk/.hidden/babelfishplugin.desktop
%{_datadir}/applnk/.hidden/crashesplugin.desktop
%{_datadir}/applnk/.hidden/dirfilterplugin.desktop
%{_datadir}/applnk/.hidden/domtreeviewerplugin.desktop
%{_datadir}/applnk/.hidden/kcmkuick.desktop
%{_datadir}/applnk/.hidden/khtmlsettingsplugin.desktop
%{_datadir}/applnk/.hidden/kimgalleryplugin.desktop
%{_datadir}/applnk/.hidden/kuickplugin.desktop
%{_datadir}/applnk/.hidden/mediaplayerplugin.desktop
%{_datadir}/applnk/.hidden/minitoolsplugin.desktop
%{_datadir}/applnk/.hidden/smbmounterplugin.desktop
%{_datadir}/applnk/.hidden/uachangerplugin.desktop
%{_datadir}/applnk/.hidden/validatorsplugin.desktop
%{_datadir}/applnk/.hidden/webarchiverplugin.desktop
%{_datadir}/applnk/.hidden/searchbarplugin.desktop
%{_iconsdir}/crystalsvg/*/actions/babelfish.png
%{_iconsdir}/crystalsvg/*/actions/cssvalidator.png
%{_iconsdir}/crystalsvg/*/actions/domtreeviewer.png
%{_iconsdir}/crystalsvg/*/actions/htmlvalidator.png
%{_iconsdir}/crystalsvg/*/actions/imagegallery.png
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
#%{_datadir}/apps/konqsidebartng/entries/news.desktop
%{_datadir}/apps/konqueror/icons/crystalsvg/16x16/actions/google.png
%{_datadir}/config.kcfg/konq_sidebarnews.kcfg
%{_iconsdir}/crystalsvg/*/apps/konqsidebar_news.png

#%files kontact
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kcm_kontactknt.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kontactknt.so
#%{_libdir}/kde3/libkontact_newstickerplugin.la
#%attr(755,root,root) %{_libdir}/kde3/libkontact_newstickerplugin.so
#%{_datadir}/services/kcmkontactknt.desktop
#%{_datadir}/services/kontact/newstickerplugin.desktop

%files ksig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksig
%{_datadir}/apps/ksig
%{_desktopdir}/kde/ksig.desktop
%{_iconsdir}/*/*/apps/ksig.png
%{_mandir}/man1/ksig.1*

%files kvim
%defattr(644,root,root,755)
%{_libdir}/libxvim.la
# What to do wit it?
%attr(755,root,root) %{_libdir}/libxvim.so
#
%attr(755,root,root) %{_libdir}/libxvim.so.*.*.*
%{_libdir}/kde3/kcm_vim.la
%attr(755,root,root) %{_libdir}/kde3/kcm_vim.so
%{_libdir}/kde3/libvimpart.la
%attr(755,root,root) %{_libdir}/kde3/libvimpart.so*
%{_datadir}/apps/kcontrol/pics/kvim.png
%{_datadir}/apps/vimpart
%{_datadir}/services/vimpart.desktop
%{_desktopdir}/kde/kcmvim.desktop

%files lnkforward
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lnkforward
%{_libdir}/kde3/kfile_lnk.la
%attr(755,root,root) %{_libdir}/kde3/kfile_lnk.so
%{_libdir}/kde3/librellinksplugin.la
%attr(755,root,root) %{_libdir}/kde3/librellinksplugin.so
%{_desktopdir}/kde/lnkforward.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_rellinks.rc
%{_datadir}/mimelnk/application/x-win-lnk.desktop
%{_datadir}/services/kfile_lnk.desktop
%{_mandir}/man1//lnkforward.1*

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
