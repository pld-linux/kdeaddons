%define sourcedir stable/%{version}/distribution/tar/generic/source
Version: 2.2.1
%define DATE 20010724
%define is_release 1
%define beta %{nil}
%define rel 1
%define ver %{version}%{beta}
%if "%{beta}" != ""
Release: 0.%{beta}.%{rel}
%else
%if %{is_release}
Release: %{rel}
%else
Release: 0.cvs%{DATE}.%{rel}
%endif
%endif

Name: kdeaddons
Prefix: /usr
Requires: kdebase >= 2.2 kdelibs >= 2.2 SDL >= 1.2.0
BuildPrereq: kdebase-devel >= 2.2 kdemultimedia-devel >= 2.2 qt-devel >= 2.2.0 zlib-devel libpng-devel libmng-devel SDL-devel >= 1.2.0 kdemultimedia >= 2.2
%if %{is_release}
Source: ftp://ftp.kde.org/pub/kde/%{sourcedir}/%{name}-%{ver}.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/%{sourcedir}/%{name}-%{DATE}.tar.bz2
%endif
Summary: K Desktop Environment - Plugins
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL

%description
Plugins for some KDE applications: %{name} extends the functionality
of Konqueror (web browser and file manager), noatun (media player)
and Kate (text editor).

%package kate
Summary: Plugins for the Kate text editor
Group: User Interface/Desktops
Requires: kdebase >= 2.2

%description kate
%{name}-kate contains plugins extending the functionality of the Kate
(KDE Advanced Text Editor) editor.
%{name}-kate adds, among other things, DCOP support, project management
and text filtering capabilities.

%package kicker
Summary: Plugins and additional applets for Kicker (the KDE panel)
Group: User Interface/Desktops
Requires: kdebase >= 2.2

%description kicker
Plugins and additional applets for Kicker (the KDE panel)

%package knewsticker
Summary: Scripts extending the functionality of KNewsTicker
Group: User Interface/Desktops
Requires: kdebase >= 2.2 kdenetwork >= 2.2

%description knewsticker
Scripts extending the functionality of KNewsTicker

%package konqueror
Summary: Plugins extending the functionality of Konqueror
Group: User Interface/Desktops
Requires: kdebase >= 2.2

%description konqueror
Plugins extending the functionality of Konqueror.
%{name}-konqueror contains, among other things, plugins for translating web
pages, checking web pages for valid HTML code, and viewing the DOM tree of
web pages.

%package noatun
Summary: Plugins extending the functionality of the noatun media player
Group: Applications/Multimedia
Requires: kdemultimedia >= 2.2

%description noatun
Plugins extending the functionality of the noatun media player

%prep
rm -rf $RPM_BUILD_ROOT

%if %{is_release}
%setup -q -n %{name}-%{ver}
%else
%setup -q -n %{name}
%endif
make -f Makefile.cvs

%build
export KDEDIR=%{prefix}
unset QTDIR || : ; . /etc/profile.d/qt.sh

CXXFLAGS="$RPM_OPT_FLAGS -DNDEBUG -DNO_DEBUG -fno-check-new" CFLAGS="$RPM_OPT_FLAGS -DNDEBUG -DNO_DEBUG" \
./configure --prefix=%{prefix} --includedir=%{prefix}/include/kde --enable-final
make %{?_smp_mflags}
make -C noatun-plugins %{?_smp_mflags}

%install
make install-strip DESTDIR=$RPM_BUILD_ROOT
make -C noatun-plugins install-strip DESTDIR=$RPM_BUILD_ROOT
# Make symlinks relative
cd $RPM_BUILD_ROOT%{prefix}/share/doc/HTML/en
for i in *; do
	[ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
done

%clean
rm -rf $RPM_BUILD_ROOT

%files kate
%defattr(-,root,root)
%{prefix}/bin/dcop_kate
%{prefix}/bin/testor
%{prefix}/lib/kde2/libkate*
%dir /usr/share/apps/kate/plugins
%{prefix}/share/apps/kate/plugins/*
%doc %{prefix}/share/doc/HTML/en/kate-plugins/*

%files kicker
%defattr(-,root,root)
%{prefix}/lib/libktimemon*
%{prefix}/lib/libkolourpicker*
%{prefix}/share/icons/*/*/*/ktimemon.png
%{prefix}/share/apps/kicker/applets/*
%doc %{prefix}/share/doc/HTML/en/kicker-applets/*

%files knewsticker
%defattr(-,root,root)
%dir %{prefix}/share/apps/knewsticker/scripts
%{prefix}/share/apps/knewsticker/scripts/*

%files konqueror
%defattr(-,root,root)
%{prefix}/lib/kde2/libkhtml*
%{prefix}/lib/kde2/libkimg*
%{prefix}/lib/kde2/libdirfilter*
%{prefix}/lib/kde2/libuachanger*
%{prefix}/lib/kde2/libbabelfish*
%{prefix}/lib/kde2/libvalidator*
%{prefix}/lib/kde2/libdomtree*
%{prefix}/lib/kde2/*webarchive*
%dir %{prefix}/share/apps/khtml/kpartplugins
%{prefix}/share/apps/khtml/kpartplugins/*
%{prefix}/share/apps/konqiconview/kpartplugins/*
%{prefix}/share/apps/konqlistview/kpartplugins/*
%{prefix}/share/icons/*/*/*/imagegallery*
%{prefix}/share/icons/*/*/*/babelfish*
%{prefix}/share/icons/*/*/*/validators*
%{prefix}/share/icons/*/*/*/cssvalidator*
%{prefix}/share/icons/*/*/*/htmlvalidator*
%{prefix}/share/icons/*/*/*/domtreeviewer*
%{prefix}/share/icons/*/*/*/webarchiver*
%{prefix}/share/mimelnk/application/*webarchive*
%{prefix}/share/services/webarchive*

%files noatun
%defattr(-,root,root)
%{prefix}/lib/libnoatun*
%{prefix}/share/apps/noatun/*
%{prefix}/bin/noatun*

%changelog
* Mon Sep 17 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2.1-1
- 2.2.1

* Thu Aug  9 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-2
- Own some directories (#51196)
- Remove ia64 workarounds, no longer needed

* Mon Aug  6 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-1
- 2.2 final

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010724.1
- Require kdemultimedia-devel >= 2.2 rather than just kdemultimedia-devel
- Update

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010723.1
- Update
- Split in subpackages

* Thu Apr 26 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Initial release
