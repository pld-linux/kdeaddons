Summary:	K Desktop Environment - Plugins
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pl):	Wtyczki do aplikacji KDE
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeaddons
Version:	2.2.2
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdebase-devel >= 2.2
# YES, it requires kdebase --- it contains some .so files. And 
# kdebase-devel contains only headers thus it doesn't require kdebase.
BuildRequires:	kdebase >= 2.2
BuildRequires:	kdemultimedia-devel >= 2.2
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
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações

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
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações

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
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações

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
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações

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
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações

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

%{__make} -f Makefile.cvs

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final

%{__make}
%{__make} -C noatun-plugins

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C noatun-plugins install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang kate-plugins --with-kde
%find_lang kicker-applets --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files kate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop_kate
%attr(755,root,root) %{_bindir}/testor
%{_libdir}/kde2/libkate*
%dir %{_datadir}/apps/kate/plugins
%{_datadir}/apps/kate/plugins/*

%files kicker
%defattr(644,root,root,755)
%{_libdir}/libktimemon*
%{_libdir}/libkolourpicker*
%{_pixmapsdir}/*/*/*/ktimemon.png
%{_datadir}/apps/kicker/applets/*

%files knewsticker
%defattr(644,root,root,755)
%dir %{_datadir}/apps/knewsticker/scripts
%{_datadir}/apps/knewsticker/scripts/*

%files konqueror
%defattr(644,root,root,755)
%{_libdir}/kde2/libkhtml*
%{_libdir}/kde2/libkimg*
%{_libdir}/kde2/libdirfilter*
%{_libdir}/kde2/libuachanger*
%{_libdir}/kde2/libbabelfish*
%{_libdir}/kde2/libvalidator*
%{_libdir}/kde2/libdomtree*
%{_libdir}/kde2/*webarchive*
%dir %{_datadir}/apps/khtml/kpartplugins
%{_datadir}/apps/khtml/kpartplugins/*
%{_datadir}/apps/konqiconview/kpartplugins/*
%{_datadir}/apps/konqlistview/kpartplugins/*
%{_pixmapsdir}/*/*/*/imagegallery*
%{_pixmapsdir}/*/*/*/babelfish*
%{_pixmapsdir}/*/*/*/validators*
%{_pixmapsdir}/*/*/*/cssvalidator*
%{_pixmapsdir}/*/*/*/htmlvalidator*
%{_pixmapsdir}/*/*/*/domtreeviewer*
%{_pixmapsdir}/*/*/*/webarchiver*
%{_datadir}/mimelnk/application/*webarchive*
%{_datadir}/services/webarchive*

%files noatun
%defattr(644,root,root,755)
%{_libdir}/libnoatun*
%{_datadir}/apps/noatun/*
%attr(755,root,root) %{_bindir}/noatun*
