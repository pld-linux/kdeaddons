#
# TODO:
# Splitting konqueror subpackage
#
# Conditional build:
%bcond_without  i18n    # don't build i18n subpackages
#
%define		_state		stable
%define		_ver		3.2.0
##%define		_snap		040110

Summary:	K Desktop Environment - Plugins
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pl):	Wtyczki do aplikacji KDE
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicaçőes KDE
Name:		kdeaddons
Version:	%{_ver}
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	e61991c52aa6b76dec0790e76eb889bd
%if %{with i18n}
Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	464451c674acd4bb27e0e34a48d737e2
%endif
Patch0:		http://rambo.its.tudelft.nl/~ewald/xine/%{name}-3.1.0-sidebar-video.patch
BuildRequires:	SDL-devel
BuildRequires:	automake
BuildRequires:	db-cxx-devel
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= 9:%{version}
BuildRequires:	kdegames-devel >= 8:%{version}
BuildRequires:	kdemultimedia-devel >= 9:%{version}
BuildRequires:	kdenetwork-devel >= 10:%{version}
BuildRequires:	kdepim-devel >= 3:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for some KDE applications: %{name} extends the functionality
of Konqueror (web browser and file manager), noatun (media player) and
Kate (text editor).

%description -l pl
Wtyczki dla niektórych aplikacji KDE, rozszerzające funkcjonalność
Konquerora (przeglądarki WWW i zarządcy plików), noatun (odtwarzacza
plików multimedialnych), Kate (edytora tekstu).

%description -l pt_BR
kdeaddons contem plugins e scripts adicionais para alguma aplicaçőes
KDE.

%package atlantikdesigner
Summary:	Atlantik board designer
Summary(pl):	Program do tworzenia plansz dla gry Atlantik
Group:		X11/Applications/Games
Requires:	kdegames-atlantik >= 8:%{version}

%description atlantikdesigner
Atlantik board designer.

%description atlantikdesigner -l pl
Program do tworzenia plansz dla gry Atlantik.

%package fsview
Summary:	FSView - a tool for showing disc utilization in a graphical form
Summary(pl):	FSview - narzędzie do graficznego przedstawiania wolnego miejsca na dysku
Group:		X11/Applications
Requires:	konqueror >= 9:%{version}

%description fsview
FSView is a tool for showing disc utilization in a graphical form,
much like the UNIX command 'du'.

%description fsview -l pl
FSview służy do graficznego przedstawiania wolnego miejsca na dysku,
działa podobnie do polecenia 'du'.

%package kaddressbook-plugins
Summary:	Plugins for kaddressbook
Summary(es):	Plugins para kaddressbook
Summary(pl):	Wtyczki do kaddressbook
Summary(pt_BR):	Plugins para kaddressbook
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3:%{version}

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
Requires:	kdebase-kate >= 9:%{version}

%description kate
kdeaddons-kate contains plugins extending the functionality of the
Kate (KDE Advanced Text Editor) editor. kdeaddons-kate adds, among
other things, DCOP support, project management and text filtering
capabilities.

%description kate -l es
Este paquete prove plugins de KDE para kdebase-kate.

%description kate -l pl
Ten pakiet zawiera wtyczki rozszerzające funkcjonalność Kate (KDE
Advanced Text Editor - Zaawansowanego Edytora Tekstów KDE). Dodaje
m.in. obsługę DCOP, możliwość zarządzania projektami i filtrowania
tekstu.

%description kate -l pt_BR
Este pacote fornece plugins KDE para kdebase-kate.

%package kicker
Summary:	Plugins and additional applets for Kicker (the KDE panel)
Summary(es):	Plugins para kdebase-kicker
Summary(pl):	Wtyczki i dodatkowe aplety do Kickera (panelu KDE)
Summary(pt_BR):	Plugins para kdebase-kicker
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

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
Summary(pl):	Skrypty rozszerzające funkcjonalność KNewsTickera
Group:		X11/Applications
Requires:	kdenetwork-knewsticker >= 10:%{version}

%description knewsticker
Scripts extending the functionality of KNewsTicker.

%description knewsticker -l pl
Skrypty rozszerzające funkcjonalność KNewsTickera.

%package konqueror
Summary:	Plugins extending the functionality of Konqueror
Summary(es):	Plugins para konqueror
Summary(pl):	Wtyczki rozszerzające funkcjonalność Konquerora
Summary(pt_BR):	Plugins para konqueror
Group:		X11/Applications
Requires:	konqueror >= 9:%{version}

%description konqueror
Plugins extending the functionality of Konqueror. %{name}-konqueror
contains, among other things, plugins for translating web pages,
checking web pages for valid HTML code, and viewing the DOM tree of
web pages.

%description konqueror -l es
Este paquete prove plugins de KDE para kdebase-konqueror.

%description konqueror -l pl
Pakiet zawiera wtyczki rozszerzające funkcjonalność Konquerora.
Zawiera m.in. wtyczki do tłumaczenia stron WWW, sprawdzania
poprawności HTML, oglądania drzewa DOM stron WWW.

%description konqueror -l pt_BR
Este pacote fornece plugins KDE para kdebase-konqueror.

%package kontact
Summary:	Plugins extending the functionality of Kontact
Summary(pl):	Wtyczki rozszerzające funkcjonalność Kontact
Group:		X11/Applications
Requires:	kdepim-kontact >= 3:%{version}
Requires:	kdenetwork-knewsticker >= 10:%{version}

%description kontact
Plugins extending the functionality of Kontact. This includes an
rss feeds module.

%description kontact -l pl
Wtyczki rozszerzające funkcjonalność Kontact. Pakiet zawiera
moduł wyświetlający źródła rss.

%package ksig
Summary:	A signature creator and manager
Summary(pl):	Program tworzący i zarządzający podpisami
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description ksig
A signature creator and manager.

%description ksig -l pl
Program tworzący i zarządzający podpisami.

%package kvim
Summary:	Vim KPart
Summary(pl):	KPart z vimem
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kvim
A kpart allowing KDE apps to embedd vim as an editor.

%description kvim -l pl
KPart umożliwiający aplikacjom KDE wykorzystywanie vima jako
osadzonego edytora.

%package noatun
Summary:	Plugins extending the functionality of the noatun media player
Summary(es):	Plugins para kdemultimedia-noatun
Summary(pl):	Wtyczki rozszerzające funkcjonalność odtwarzacza noatun
Summary(pt_BR):	Plugins para kdemultimedia-noatun
Group:		X11/Applications
Requires:	kdemultimedia-noatun >= 9:%{version}

%description noatun
Plugins extending the functionality of the noatun media player.

%description noatun -l es
Este paquete prove plugins de KDE para kdemultimedia-noatun.

%description noatun -l pl
Wtyczki rozszerzające funkcjonalność odtwarzacza plików
multimedialnych noatun.

%description noatun -l pt_BR
Este pacote fornece plugins KDE para kdemultimedia-noatun.

%package i18n
Summary:	Common internationalization and localization files for kdeaddons
Summary(pl):	Współdzielone pliki umiędzynarodawiające dla kdeaddons
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdeaddons.

%description i18n -l pl
Współdzielone pliki umiędzynarodawiające dla kdeaddons.

%package atlantikdesigner-i18n
Summary:	Internationalization and localization files for atlantikdesigner
Summary(pl):	Pliki umiędzynarodawiające dla atlantikdesigner
Group:		X11/Applications
Requires:	%{name}-atlantikdesigner = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdegames-atlantik-i18n >= 9:%{version}

%description atlantikdesigner-i18n
Internationalization and localization files for atlantikdesigner.

%description atlantikdesigner-i18n -l pl
Pliki umiędzynarodawiające dla atlantikdesigner.

%package kontact-i18n
Summary:	Internationalization and localization files for kontact
Summary(pl):	Pliki umiędzynarodawiające dla kontact
Group:		X11/Applications
Requires:	%{name}-kontact = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-kontact-i18n >= 9:%{version}
Requires:	kdenetwork-knewsticker-i18n >= 9:%{version}

%description kontact-i18n
Internationalization and localization files for kontact.

%description kontact-i18n -l pl
Pliki umiędzynarodawiające dla kontact.

%package ksig-i18n
Summary:	Internationalization and localization files for ksig
Summary(pl):	Pliki umiędzynarodawiające dla ksig
Group:		X11/Applications
Requires:	%{name}-ksig = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ksig-i18n
Internationalization and localization files for ksig.

%description ksig-i18n -l pl
Pliki umiędzynarodawiające dla ksig.

%package kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl):	Pliki umiędzynarodawiające dla kaddressbook
Group:		X11/Applications
Requires:	%{name}-kaddressbook = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdepim-kaddressbook-i18n >= 9:%{version}

%description kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description kaddressbook-i18n -l pl
Pliki umiędzynarodawiające dla kaddressbook.

%package kate-i18n
Summary:	Internationalization and localization files for kate
Summary(pl):	Pliki umiędzynarodawiające dla kate
Group:		X11/Applications
Requires:	%{name}-kate = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kate-i18n >= 9:%{version}

%description kate-i18n
Internationalization and localization files for kate.

%description kate-i18n -l pl
Pliki umiędzynarodawiające dla kate.

%package fsview-i18n
Summary:	Internationalization and localization files for fsview
Summary(pl):	Pliki umiędzynarodawiające dla fsview
Group:		X11/Applications
Requires:	%{name}-fsview = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n >= 9:%{version}

%description fsview-i18n
Internationalization and localization files for fsview.

%description fsview-i18n -l pl
Pliki umiędzynarodawiające dla fsview.

%package noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl):	Pliki umiędzynarodawiające dla noatun
Group:		X11/Applications
Requires:	%{name}-noatun = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdemultimedia-noatun-i18n >= 9:%{version}

%description noatun-i18n
Internationalization and localization files for noatun.

%description noatun-i18n -l pl
Pliki umiędzynarodawiające dla noatun.

%package kvim-i18n
Summary:	Internationalization and localization files for kvim
Summary(pl):	Pliki umiędzynarodawiające dla kvima
Group:		X11/Applications
Requires:	%{name}-kvim = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kvim-i18n
Internationalization and localization files for kvim.

%description kvim-i18n -l pl
Pliki umiędzynarodawiające dla kvima.

%package kicker-i18n
Summary:	Internationalization and localization files for kicker
Summary(pl):	Pliki umiędzynarodawiające dla kickera
Group:		X11/Applications
Requires:	%{name}-kicker = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}

%description kicker-i18n
Internationalization and localization files for kicker.

%description kicker-i18n -l pl
Pliki umiędzynarodawiające dla kickera.

%package konqueror-i18n
Summary:	Internationalization and localization files for konqueror
Summary(pl):	Pliki umiędzynarodawiające dla konquerora
Group:		X11/Applications
Requires:	%{name}-konqueror = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n >= 9:%{version}

%description konqueror-i18n
Internationalization and localization files for konqueror.

%description konqueror-i18n -l pl
Pliki umiędzynarodawiające dla konquerora.

%prep
%setup -q 
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

mv $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color/16x16/apps/autorefresh.png

%find_lang	kate-plugins	--with-kde
%find_lang	kicker-applets	--with-kde
%find_lang	konq-plugins	--with-kde

%if %{with i18n}
%find_lang	fsview		--with-kde
%find_lang	desktop_kdeaddons	--with-kde
%find_lang	atlantikdesigner	--with-kde
%find_lang	kcmkontactnt		--with-kde
%find_lang	ksig		--with-kde
%find_lang	libkaddrbk_geo_xxport	--with-kde

kicker="kbinaryclock \
kolourpicker \
ktimemon \
mediacontrol \
kcmmediacontrol"

for i in $kicker;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kicker-applets.lang
done

vim="kcmvim \
vimpart"

for i in $vim;
do
	%find_lang $i	--with-kde
	cat $i.lang >> vim.lang
done

noatun="alsaplayerui \
charlatanui \
dub \
ffrs \
jefferson \
lyrics \
nexscope \
pitchablespeed \
synaescope \
tippecanoe \
tyler \
wakeup \
wavecapture"

for i in $noatun;
do
	%find_lang $i	--with-kde
	cat $i.lang >> noatun.lang
done

konqueror="khtmlsettingsplugin \
konqsidebar_mediaplayer \
konq_smbmounterplugin \
validatorsplugin \
webarchiver \
autorefresh \
babelfish \
crashesplugin \
dirfilterplugin \
domtreeviewer \
imgalleryplugin \
kcmkuick \
minitoolsplugin \
uachangerplugin \
kuick_plugin \
audiorename_plugin \
imagerename_plugin \
kfile_desktop \
kfile_folder \
kfile_html \
kfile_txt"

for i in $konqueror;
do
	%find_lang $i	--with-kde
	cat $i.lang >> konq-plugins.lang
done

kate="katecppsymbolviewer \
katefll_initplugin \
katefll_plugin \
katehelloworld \
katehtmltools \
kateinsertcommand \
katemake \
katemodeline \
kateopenheader \
kateprojectmanager \
katepybrowse \
katespell \
katetextfilter \
katexmlcheck \
katexmltools"

for i in $kate;
do
	%find_lang $i	--with-kde
	cat $i.lang >> kate-plugins.lang
done
%endif

files="kate-plugins \
kicker-applets \
konq-plugins"

for i in $files; do
	> ${i}_en.lang
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with i18n}
%files i18n -f desktop_kdeaddons.lang
%files kate-i18n -f kate-plugins.lang
%files kicker-i18n -f kicker-applets.lang
%files konqueror-i18n -f konq-plugins.lang
%files atlantikdesigner-i18n -f atlantikdesigner.lang
%files kontact-i18n -f kcmkontactnt.lang
%files ksig-i18n -f ksig.lang
%files kaddressbook-i18n -f libkaddrbk_geo_xxport.lang
%files fsview-i18n -f fsview.lang
%files noatun-i18n -f noatun.lang
%files kvim-i18n -f vim.lang
%endif

%files atlantikdesigner
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atlantikdesigner
%{_datadir}/apps/atlantikdesigner
%{_desktopdir}/kde/atlantikdesigner.desktop
%{_iconsdir}/*/*/*/atlantikdesigner.png
%{_mandir}/man1/atlantikdesigner.1*

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

%files kaddressbook-plugins
%defattr(644,root,root,755)
%{_libdir}/kde3/libkaddrbk_geo_xxport.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_geo_xxport.so
%{_datadir}/apps/kaddressbook/geo_xxportui.rc
%{_datadir}/services/kaddressbook/geo_xxport.desktop

%files kate -f kate-plugins_en.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kate*.la
%attr(755,root,root) %{_libdir}/kde3/kate*.so
%{_datadir}/apps/kate/plugins
%{_datadir}/apps/kate/scripts/html-tidy.desktop
%attr(755,root,root) %{_datadir}/apps/kate/scripts/html-tidy.sh
%{_datadir}/apps/katexmltools
%{_datadir}/services/kate*
%{_datadir}/applnk/.hidden/katefll.desktop

%files kicker -f kicker-applets_en.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kolourpicker_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kolourpicker_panelapplet.so
%{_libdir}/kde3/ktimemon_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/ktimemon_panelapplet.so
%{_libdir}/kde3/kbinaryclock_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kbinaryclock_panelapplet.so
%{_libdir}/kde3/mediacontrol_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/mediacontrol_panelapplet.so
%{_datadir}/apps/kicker/applets/kolourpicker.desktop
%{_datadir}/apps/kicker/applets/ktimemon.desktop
%{_datadir}/apps/kicker/applets/mediacontrol.desktop
%{_datadir}/apps/kicker/applets/kbinaryclock.desktop
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

%files konqueror -f konq-plugins_en.lang
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
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.rc
%{_datadir}/apps/konqiconview/kpartplugins/dirfilterplugin.rc
%{_datadir}/apps/konqiconview/kpartplugins/kimgalleryplugin.rc
%{_datadir}/apps/konqiconview/kpartplugins/smbmounterplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/dirfilterplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/kimgalleryplugin.rc
%{_datadir}/apps/konqlistview/kpartplugins/smbmounterplugin.rc
%{_datadir}/apps/konqsidebartng/add/mplayer_add.desktop
%{_datadir}/apps/konqsidebartng/entries/mplayer.desktop
%{_datadir}/apps/konqsidebartng/kicker_entries/mplayer.desktop
%{_datadir}/apps/konqueror/servicemenus/imageconverter.desktop
%{_datadir}/apps/konqueror/servicemenus/jpegorient.desktop
%{_datadir}/apps/mediacontrol
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
%{_iconsdir}/crystalsvg/*/actions/babelfish.png
%{_iconsdir}/crystalsvg/*/actions/cssvalidator.png
%{_iconsdir}/crystalsvg/*/actions/domtreeviewer.png
%{_iconsdir}/crystalsvg/*/actions/htmlvalidator.png
%{_iconsdir}/crystalsvg/*/actions/imagegallery.png
%{_iconsdir}/crystalsvg/*/actions/validators.png
%{_iconsdir}/crystalsvg/*/actions/webarchiver.png
%{_iconsdir}/crystalsvg/*/apps/konqsidebar_mediaplayer.png

%files kontact
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kontactknt.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontactknt.so
%{_libdir}/kde3/libkontact_newstickerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_newstickerplugin.so
%{_datadir}/services/kcmkontactknt.desktop
%{_datadir}/services/kontact/newstickerplugin.desktop

%files ksig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksig
%{_datadir}/apps/ksig
%{_desktopdir}/kde/ksig.desktop
%{_iconsdir}/*/*/apps/ksig.png

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
%{_mandir}/man1/noatunippecanoe.bin.1*
%{_mandir}/man1/noatuntyler.bin.1*
