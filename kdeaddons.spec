Summary:	K Desktop Environment - Plugins
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeaddons
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{version}%{version}%{name}-%{version}.tar.bz2
BuildRequires:	kdebase-devel >= 2.2
BuildRequires:	kdemultimedia-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Plugins for some KDE applications: %{name} extends the functionality
of Konqueror (web browser and file manager), noatun (media player) and
Kate (text editor).

%description -l es
kdeaddons contains additional plugins and scripts for some KDE
applications.

%description -l pt_BR
kdeaddons contem plugins e scripts adicionais para alguma aplicações
KDE.

%package kate
Summary:	Plugins for the Kate text editor
Summary(es):	Plugins para kdebase-kate
Summary(pt_BR):	Plugins para kdebase-kate
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description kate
%{name}-kate contains plugins extending the functionality of the Kate
(KDE Advanced Text Editor) editor. %{name}-kate adds, among other
things, DCOP support, project management and text filtering
capabilities.

%description -l es kate
Este paquete prove plugins de KDE para kdebase-kate.

%description -l pt_BR kate
Este pacote fornece plugins KDE para kdebase-kate.

%package kicker
Summary:	Plugins and additional applets for Kicker (the KDE panel)
Summary(es):	Plugins para kdebase-kicker
Summary(pt_BR):	Plugins para kdebase-kicker
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description kicker
Plugins and additional applets for Kicker (the KDE panel)

%description -l es kicker
Este paquete prove plugins de KDE para kdebase-kicker.

%description -l pt_BR kicker
Este pacote fornece plugins KDE para kdebase-kicker.

%package knewsticker
Summary:	Scripts extending the functionality of KNewsTicker
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description knewsticker
Scripts extending the functionality of KNewsTicker.

%package konqueror
Summary:	Plugins extending the functionality of Konqueror
Summary(es):	Plugins para konqueror
Summary(pt_BR):	Plugins para konqueror
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description konqueror
Plugins extending the functionality of Konqueror. %{name}-konqueror
contains, among other things, plugins for translating web pages,
checking web pages for valid HTML code, and viewing the DOM tree of
web pages.

%description -l es konqueror
Este paquete prove plugins de KDE para kdebase-konqueror.

%description -l pt_BR konqueror
Este pacote fornece plugins KDE para kdebase-konqueror.

%package noatun
Summary:	Plugins extending the functionality of the noatun media player
Summary(es):	Plugins para kdemultimedia-noatun
Summary(pt_BR):	Plugins para kdemultimedia-noatun
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description noatun
Plugins extending the functionality of the noatun media player.

%description -l es noatun
Este paquete prove plugins de KDE para kdemultimedia-noatun.

%description -l pt_BR noatun
Este pacote fornece plugins KDE para kdemultimedia-noatun.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -DNDEBUG -DNO_DEBUG -fno-check-new" CFLAGS="%{rpmcflags} -DNDEBUG -DNO_DEBUG" \
./configure --prefix=%{_prefix} --includedir=%{_includedir}/kde --enable-final
%{__make}
%{__make} -C noatun-plugins

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C noatun-plugins install \
	DESTDIR=$RPM_BUILD_ROOT

# Make symlinks relative
cd $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en
for i in *; do
	[ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
done

%clean
rm -rf $RPM_BUILD_ROOT

%files kate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop_kate
%attr(755,root,root) %{_bindir}/testor
%{_libdir}/kde2/libkate*
%dir %{_datadir}/apps/kate/plugins
%{_datadir}/apps/kate/plugins/*
%doc %{_datadir}/doc/HTML/en/kate-plugins/*

%files kicker
%defattr(644,root,root,755)
%{_libdir}/libktimemon*
%{_libdir}/libkolourpicker*
%{_datadir}/icons/*/*/*/ktimemon.png
%{_datadir}/apps/kicker/applets/*
%doc %{_datadir}/doc/HTML/en/kicker-applets/*

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
%{_datadir}/icons/*/*/*/imagegallery*
%{_datadir}/icons/*/*/*/babelfish*
%{_datadir}/icons/*/*/*/validators*
%{_datadir}/icons/*/*/*/cssvalidator*
%{_datadir}/icons/*/*/*/htmlvalidator*
%{_datadir}/icons/*/*/*/domtreeviewer*
%{_datadir}/icons/*/*/*/webarchiver*
%{_datadir}/mimelnk/application/*webarchive*
%{_datadir}/services/webarchive*

%files noatun
%defattr(644,root,root,755)
%{_libdir}/libnoatun*
%{_datadir}/apps/noatun/*
%attr(755,root,root) %{_bindir}/noatun*
