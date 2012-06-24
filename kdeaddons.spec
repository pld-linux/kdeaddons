Summary:	K Desktop Environment - Plugins
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pl):	Wtyczki do aplikacji KDE
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplica��es KDE
Name:		kdeaddons
Version:	3.0.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-kicker-applets-no-version.patch
BuildRequires:	SDL-devel
BuildRequires:	arts-kde-devel
BuildRequires:	awk
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	kdemultimedia-devel >= 3.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	nas-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

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
Ten pakiet zawiera wtyczki rozszerzaj�ce funkcjonalno�� Kate (KDE
Advanced Text Editor - zaawansowanego edytora tekst�w KDE). Dodaje
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
poprawno�ci HTML, ogl�dania drzewa DOM stron WWW.

%description konqueror -l pt_BR
Este pacote fornece plugins KDE para kdebase-konqueror.

%package noatun
Summary:	Plugins extending the functionality of the noatun media player
Summary(es):	Plugins para kdemultimedia-noatun
Summary(pl):	Wtyczki rozszerzaj�ce funkcjonalno�� odtwarzacza noatun
Summary(pt_BR):	Plugins para kdemultimedia-noatun
Group:		X11/Applications

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
%patch0 -p1

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
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings/KDE,%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C noatun-plugins install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/FileBrowsing \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

> kate.lang
programs="katehelloworld katehtmltools kateinsertcommand kateopenheader kateprojectmanager katetextfilter katexmltools"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kate.lang
done

> konqueror.lang
programs="babelfish dirfilterplugin domtreeviewer dub imgalleryplugin kcmkuick khtmlsettingsplugin konqsidebar_mediaplayer kuick_plugin uachangerplugin validatorsplugin webarchiver"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> konqueror.lang
done

%find_lang kicker-applets --with-kde
%find_lang konq-plugins --with-kde
%find_lang kolourpicker --with-kde
%find_lang ktimemon --with-kde
cat kicker-applets.lang kolourpicker.lang ktimemon.lang > kicker.lang
cat konq-plugins.lang >> konqueror.lang
%clean
rm -rf $RPM_BUILD_ROOT

%files kate -f kate.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop_kate
%attr(755,root,root) %{_bindir}/testor
%{_libdir}/kde3/kate*.??
%dir %{_datadir}/apps/kate/plugins
%{_datadir}/apps/kate/plugins/*
%{_datadir}/apps/katexmltools
/usr/share/doc/kde/HTML/en/kate-plugins/*

%files kicker -f kicker.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/*_panelapplet.??
%{_pixmapsdir}/*/*/*/ktimemon.png
%{_datadir}/apps/kicker/applets/*

%files knewsticker
%defattr(644,root,root,755)
%dir %{_datadir}/apps/knewsticker/scripts
%{_datadir}/apps/knewsticker/scripts/*

%files konqueror -f konqueror.lang
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
%{_datadir}/apps/konqsidebartng/add/*
%{_datadir}/apps/konqsidebartng/entries/*
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
%{_applnkdir}/Settings/KDE/FileBrowsing/kcmkuick.desktop

%files noatun
%defattr(644,root,root,755)
%{_libdir}/kde3/noatun*.??
%{_datadir}/apps/noatun/*
%attr(755,root,root) %{_bindir}/noatun*
%{_mandir}/man1/noatun*
