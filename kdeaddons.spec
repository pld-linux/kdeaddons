%define		_ver		3.0
#define		_sub_ver
%define		_rel		1

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	K Desktop Environment - Plugins
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pl):	Wtyczki do aplikacji KDE
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeaddons
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	arts-kde-devel
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	kdemultimedia-devel >= 3.0
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Plugins for some KDE applications: %{name} extends the functionality
of Konqueror (web browser and file manager), noatun (media player) and
Kate (text editor).

%description -l es
kdeaddons contains additional plugins and scripts for some KDE
applications.

%description -l pl
Wtyczki dla niektórych aplikacji KDE, rozszerzaj±ce funkcjonalno¶æ
Konquerora (przegl±darki WWW i menad¿era plików), noatun (odtwarzacza
plików multimedialnych), Kate (edytora tekstu).

%description -l pt_BR
kdeaddons contem plugins e scripts adicionais para alguma aplicações
KDE.

%package kate
Summary:	Plugins for the Kate text editor
Summary(es):	Plugins para kdebase-kate
Summary(pl):	Wtyczki do edytora tekstu Kate
Summary(pt_BR):	Plugins para kdebase-kate
Group:		X11/Applications

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
poprawno¶ci HTML, ogl±dania drzewa DOM dokumentów.

%description konqueror -l pt_BR
Este pacote fornece plugins KDE para kdebase-konqueror.

%package noatun
Summary:	Plugins extending the functionality of the noatun media player
Summary(es):	Plugins para kdemultimedia-noatun
Summary(pl):	Wtyczki rozszerzaj±ce funkcjonalno¶æ odtwarzacza noatun
Summary(pt_BR):	Plugins para kdemultimedia-noatun
Group:		X11/Applications

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

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final

%{__make}
%{__make} -C noatun-plugins

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/KDE

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C noatun-plugins install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}{,/KDE}/Settings

%find_lang kate-plugins --with-kde
%find_lang kicker-applets --with-kde
%find_lang konq-plugins --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files kate -f kate-plugins.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop_kate
%attr(755,root,root) %{_bindir}/testor
%{_libdir}/kde3/kate*.??
%dir %{_datadir}/apps/kate/plugins
%{_datadir}/apps/kate/plugins/*
%{_datadir}/apps/katexmltools

%files kicker -f kicker-applets.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/*_panelapplet.??
%{_libdir}/kde3/*_panelapplet.so.*.*.*
%{_pixmapsdir}/*/*/*/ktimemon.png
%{_datadir}/apps/kicker/applets/*

%files knewsticker
%defattr(644,root,root,755)
%dir %{_datadir}/apps/knewsticker/scripts
%{_datadir}/apps/knewsticker/scripts/*

%files konqueror -f konq-plugins.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/konq*.??
%{_libdir}/kde3/libkhtml*
%{_libdir}/kde3/libkimg*
%{_libdir}/kde3/libdirfilter*
%{_libdir}/kde3/libuachanger*
%{_libdir}/kde3/libbabelfish*
%{_libdir}/kde3/libvalidator*
%{_libdir}/kde3/libdomtree*
%{_libdir}/kde3/*webarchive*
%{_libdir}/kde3/libkcm_*.??
%{_libdir}/kde3/libkuickplugin.??
%dir %{_datadir}/apps/khtml/kpartplugins
%{_datadir}/apps/khtml/kpartplugins/*
%{_datadir}/apps/konqiconview/kpartplugins/*
%{_datadir}/apps/konqlistview/kpartplugins/*
%{_datadir}/apps/konqsidebartng
%{_pixmapsdir}/*/*/*/babelfish*
%{_pixmapsdir}/*/*/*/cssvalidator*
%{_pixmapsdir}/*/*/*/domtreeviewer*
%{_pixmapsdir}/*/*/*/htmlvalidator*
%{_pixmapsdir}/*/*/*/imagegallery*
%{_pixmapsdir}/*/*/*/konqsidebar_mediaplayer*
%{_pixmapsdir}/*/*/*/validators*
%{_pixmapsdir}/*/*/*/webarchiver*
%{_datadir}/mimelnk/application/*webarchive*
%{_datadir}/services/webarchive*
%{_datadir}/services/kuickplugin*
%{_applnkdir}/KDE/Settings/FileBrowsing/kcmkuick.desktop

%files noatun
%defattr(644,root,root,755)
%{_libdir}/kde3/noatun*.??
%{_datadir}/apps/noatun/*
%attr(755,root,root) %{_bindir}/noatun*
