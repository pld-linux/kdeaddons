#
# TODO:
# Splitting konqueror subpackage

%define		_state		stable
%define		_ver		3.1.5

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
# Source0-md5:	789f4ff2037a9ce1ae0219f7e2fc4db6
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	edbce651684941ab44d5560143bd8c9c
Source2:	%{name}-atlantikdesigner.png
#Source3:	%{name}-editcopy.png
Patch0:		http://rambo.its.tudelft.nl/~ewald/xine/%{name}-3.1.0-sidebar-video.patch
BuildRequires:	SDL-devel
BuildRequires:	arts-kde-devel
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= %{version}
#BuildRequires:	kdebase-libkate >= %{version}
BuildRequires:	kdemultimedia-devel >= %{version}
BuildRequires:	kdegames-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
#BuildRequires:	nas-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
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
Summary:	Atlantik board designer
Summary(pl):	Program do tworzenia plansz dla gry Atlantik
Group:		X11/Applications/Games
Requires:	kdegames-atlantik >= %{version}

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
Requires:	kdebase-kate >= 8:%{version}

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
Requires:	kdebase-kicker >= 8:%{version}

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
Requires:	kdenetwork-knewsticker >= %{version}

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
Requires:	konqueror >= 8:%{version}

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
Requires:	kdemultimedia-noatun >= %{version}

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

for plik in `find . -name \*.desktop | xargs grep -l '\[nb\]'` ; do
	echo -e ',s/\[nb\]=/[no]=/\n,w' | ed $plik 2>/dev/null
done

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/atlantikdesigner.png
#install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/editcopy.png

for i in `find $RPM_BUILD_ROOT%{_applnkdir} -type f`; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

> kate.lang
programs=" \
	kate-plugins \
	katefll_initplugin \
	katefll_plugin \
	katehtmltools \
	kateinsertcommand \
	katemodeline \
	kateopenheader \
	katepybrowse \
	katespell \
	katetextfilter \
	katexmlcheck \
	katexmltools"
# does not build
#	katehelloworld
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kate.lang
done

> konqueror.lang
programs=" \
	babelfish \
	dirfilterplugin \
	domtreeviewer \
	imgalleryplugin \
	kcmkuick \
	kfile_desktop \
	kfile_folder \
	kfile_html \
	kfile_txt \
	khtmlsettingsplugin \
	konqsidebar_mediaplayer \
	kuick_plugin \
	uachangerplugin \
	validatorsplugin \
	webarchiver"
# does not build
#	crashesplugin
for i in $programs; do
	%find_lang $i
	cat $i.lang >> konqueror.lang
done
%find_lang	konq-plugins	--with-kde
cat konq-plugins.lang >> konqueror.lang

>kicker.lang
programs=" \
	kicker-applets \
	kolourpicker \
	ktimemon \
	mediacontrol"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kicker.lang
done

>noatun.lang
programs=" \
	alsaplayerui \
	charlatanui \
	ffrs \
	lyrics \
	pitchablespeed \
	synaescope \
	tippecanoe \
	tyler \
	wakeup \
	wavecapture"
# do not build
#	dub
#	jefferson
#	nexscope
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> noatun.lang
done

%find_lang	atlantikdesigner	--with-kde

# does not build
#%find_lang	imagerename_plugin	--with-kde

# probably obsolete
#%find_lang	kateisearch		--with-kde
#%find_lang	kateprojectmanager	--with-kde

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files atlantikdesigner -f atlantikdesigner.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atlantikdesigner
%{_datadir}/apps/atlantikdesigner
%{_applnkdir}/Games/Board/*
%{_pixmapsdir}/*/*/*/atlantikdesigner.png
%{_pixmapsdir}/atlantikdesigner.png
%{_mandir}/man1/atlantikdesigner.*

%files kate -f kate.lang
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/dcop_kate
#%attr(755,root,root) %{_bindir}/testor
%{_libdir}/kde3/kate*.la
%attr(755,root,root) %{_libdir}/kde3/kate*.so
%{_datadir}/apps/kate/plugins
%{_datadir}/apps/katexmltools
%{_datadir}/services/kate*
%{_applnkdir}/Editors/katefll.desktop

%files kicker -f kicker.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/*_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/*_panelapplet.so
%{_pixmapsdir}/[!l]*/*/*/ktimemon.png
%{_datadir}/apps/kicker/applets/*

%files knewsticker
%defattr(644,root,root,755)
%dir %{_datadir}/apps/knewsticker/scripts
%{_datadir}/apps/knewsticker/scripts/*

%files konqueror -f konqueror.lang
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
%{_applnkdir}/.hidden/*
%{_pixmapsdir}/*/*/*/babelfish*
%{_pixmapsdir}/*/*/*/cssvalidator*
%{_pixmapsdir}/*/*/*/domtreeviewer*
%{_pixmapsdir}/*/*/*/htmlvalidator*
%{_pixmapsdir}/*/*/*/imagegallery*
%{_pixmapsdir}/[!l]*/*/*/konqsidebar_mediaplayer*
%{_pixmapsdir}/*/*/*/validators*
%{_pixmapsdir}/*/*/*/webarchiver*
#%{_pixmapsdir}/editcopy.png

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%{_libdir}/kde3/noatun*.la
%attr(755,root,root) %{_libdir}/kde3/noatun*.so
%{_datadir}/apps/noatun/*
%{_mandir}/man1/noatun*
