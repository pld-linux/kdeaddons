#
# TODO:
# Splitting konqueror subpackage

%define		_state		stable
%define		_ver		3.1.1

Summary:	K Desktop Environment - Plugins
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pl):	Wtyczki do aplikacji KDE
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeaddons
Version:	%{_ver}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		http://rambo.its.tudelft.nl/~ewald/xine/%{name}-3.1.0-sidebar-video.patch
BuildRequires:	SDL-devel
BuildRequires:	arts-kde-devel
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= 3.1
BuildRequires:	kdemultimedia-devel >= 3.1
BuildRequires:  kdegames-devel >= 3.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	nas-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath	1

%description
Plugins for some KDE applications: %{name} extends the functionality
of Konqueror (web browser and file manager), noatun (media player) and
Kate (text editor).

%description -l pl
Wtyczki dla niektórych aplikacji KDE, rozszerzaj±ce funkcjonalno¶æ
Konquerora (przegl±darki WWW i zarz±dcy plików), noatun (odtwarzacza
plików multimedialnych), Kate (edytora tekstu).

%description -l pt_BR
kdeaddons contem plugins e scripts adicionais para alguma aplicações
KDE.

%package atlantikdesigner
Summary:        Atlantik board designer
Summary(pl):	Program do tworzenia plansz dla gry Atlantik
Group:          X11/Applications/Games
Requires:       kdegames-atlantik

%description atlantikdesigner
Atlantik board designer.

%description atlantikdesigner -l pl
Program do tworzenia plansz dla gry Atlantik.

%package kate
Summary:	Plugins for the Kate text editor
Summary(es):	Plugins para kdebase-kate
Summary(pl):	Wtyczki do edytora tekstu Kate
Summary(pt_BR):	Plugins para kdebase-kate
Group:		X11/Applications
Requires:	kdebase-kate

%description kate
%{name}-kate contains plugins extending the functionality of the Kate
(KDE Advanced Text Editor) editor. %{name}-kate adds, among other
things, DCOP support, project management and text filtering
capabilities.

%description kate -l es
Este paquete prove plugins de KDE para kdebase-kate.

%description kate -l pl
Ten pakiet zawiera wtyczki rozszerzaj±ce funkcjonalno¶æ Kate (KDE
Advanced Text Editor - Zaawansowanego Edytora Tekstów KDE). Dodaje
m.in. obs³ugê DCOP, mo¿liwo¶æ zarz±dzania projektami i filtrowania
tekstu.

%description kate -l pt_BR
Este pacote fornece plugins KDE para kdebase-kate.

%package kicker
Summary:	Plugins and additional applets for Kicker (the KDE panel)
Summary(es):	Plugins para kdebase-kicker
Summary(pl):	Wtyczki i dodatkowe aplety do Kickera (panelu KDE)
Summary(pt_BR):	Plugins para kdebase-kicker
Group:		X11/Applications
Requires:	kdebase

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
Summary(pl):	Skrypty rozszerzaj±ce funkcjonalno¶æ KNewsTickera
Group:		X11/Applications
Requires:	kdenetwork-knewsticker

%description knewsticker
Scripts extending the functionality of KNewsTicker.

%description knewsticker -l pl
Skrypty rozszerzaj±ce funkcjonalno¶æ KNewsTickera.

%package konqueror
Summary:	Plugins extending the functionality of Konqueror
Summary(es):	Plugins para konqueror
Summary(pl):	Wtyczki rozszerzaj±ce funkcjonalno¶æ Konquerora
Summary(pt_BR):	Plugins para konqueror
Group:		X11/Applications
Requires:	konqueror

%description konqueror
Plugins extending the functionality of Konqueror. %{name}-konqueror
contains, among other things, plugins for translating web pages,
checking web pages for valid HTML code, and viewing the DOM tree of
web pages.

%description konqueror -l es
Este paquete prove plugins de KDE para kdebase-konqueror.

%description konqueror -l pl
Pakiet zawiera wtyczki rozszerzaj±ce funkcjonalno¶æ Konquerora.
Zawiera m.in. wtyczki do t³umaczenia stron WWW, sprawdzania
poprawno¶ci HTML, ogl±dania drzewa DOM stron WWW.

%description konqueror -l pt_BR
Este pacote fornece plugins KDE para kdebase-konqueror.

%package noatun
Summary:	Plugins extending the functionality of the noatun media player
Summary(es):	Plugins para kdemultimedia-noatun
Summary(pl):	Wtyczki rozszerzaj±ce funkcjonalno¶æ odtwarzacza noatun
Summary(pt_BR):	Plugins para kdemultimedia-noatun
Group:		X11/Applications
Requires:	kdemultimedia-noatun

%description noatun
Plugins extending the functionality of the noatun media player.

%description noatun -l es
Este paquete prove plugins de KDE para kdemultimedia-noatun.

%description noatun -l pl
Wtyczki rozszerzaj±ce funkcjonalno¶æ odtwarzacza plików
multimedialnych noatun.

%description noatun -l pt_BR
Este pacote fornece plugins KDE para kdemultimedia-noatun.

%prep
%setup -q
%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#> kate.lang
#programs="katehelloworld katehtmltools kateinsertcommand kateopenheader kateprojectmanager katetextfilter katexmltools"
#for i in $programs; do
#	%find_lang $i --with-kde
#	cat $i.lang >> kate.lang
#done

#> konqueror.lang
#programs="babelfish dirfilterplugin domtreeviewer dub imgalleryplugin kcmkuick khtmlsettingsplugin konqsidebar_mediaplayer kuick_plugin uachangerplugin validatorsplugin webarchiver"
#for i in $programs; do
#	%find_lang $i --with-kde
#	cat $i.lang >> konqueror.lang
#done
#
#%find_lang	atlantikdesigner --with-kde
%find_lang	kate-plugins	--with-kde
%find_lang	kicker-applets	--with-kde
%find_lang	konq-plugins	--with-kde
#%find_lang kolourpicker --with-kde
#%find_lang ktimemon --with-kde
#cat kicker-applets.lang kolourpicker.lang ktimemon.lang > kicker.lang
#cat konq-plugins.lang >> konqueror.lang

%clean
rm -rf $RPM_BUILD_ROOT

#%files  atlantikdesigner -f atlantikdesigner.lang
%files  atlantikdesigner
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atlantikdesigner
%{_pixmapsdir}/*/*/*/atlantikdesigner.png
%{_datadir}/apps/atlantikdesigner
%{_applnkdir}/Games/Board/*

#%files kate -f kate.lang
%files kate -f kate-plugins.lang
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/dcop_kate
#%attr(755,root,root) %{_bindir}/testor
%{_libdir}/kde3/kate*.la
%attr(755,root,root) %{_libdir}/kde3/kate*.so
%{_datadir}/apps/kate/plugins
%{_datadir}/apps/katexmltools
%{_datadir}/services/kate*
%{_applnkdir}/Editors/katefll.desktop

#%files kicker -f kicker.lang
%files kicker -f kicker-applets.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/*_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/*_panelapplet.so
%{_pixmapsdir}/[!l]*/*/*/ktimemon.png
%{_datadir}/apps/kicker/applets/*

%files knewsticker
%defattr(644,root,root,755)
%dir %{_datadir}/apps/knewsticker/scripts
%{_datadir}/apps/knewsticker/scripts/*

#%files konqueror -f konqueror.lang
%files konqueror -f konq-plugins.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kfile*.la
%attr(755,root,root) %{_libdir}/kde3/kfile*.so
%{_libdir}/kde3/konq*.la
%attr(755,root,root) %{_libdir}/kde3/konq*.so
%{_libdir}/kde3/[lw]*.la
%attr(755,root,root) %{_libdir}/kde3/[lw]*.so
%{_datadir}/apps/khtml/kpartplugins/*
%{_datadir}/apps/konqiconview/kpartplugins/*
%{_datadir}/apps/konqlistview/kpartplugins/*
%{_datadir}/apps/konqsidebartng/add/*
%{_datadir}/apps/konqsidebartng/entries/*
%{_datadir}/apps/mediacontrol
%{_datadir}/mimelnk/application/*webarchive*
%{_datadir}/services/kfile_*
%{_datadir}/services/kuick_plugin.desktop
%{_datadir}/services/webarchive*
%{_pixmapsdir}/*/*/*/babelfish*
%{_pixmapsdir}/*/*/*/cssvalidator*
%{_pixmapsdir}/*/*/*/domtreeviewer*
%{_pixmapsdir}/*/*/*/htmlvalidator*
%{_pixmapsdir}/*/*/*/imagegallery*
%{_pixmapsdir}/[!l]*/*/*/konqsidebar_mediaplayer*
%{_pixmapsdir}/*/*/*/validators*
%{_pixmapsdir}/*/*/*/webarchiver*
%{_applnkdir}/.hidden/*

%files noatun
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%{_libdir}/kde3/noatun*.la
%attr(755,root,root) %{_libdir}/kde3/noatun*.so
%{_datadir}/apps/noatun/*
