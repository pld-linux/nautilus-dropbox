Summary:	Dropbox extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Dropbox dla Nautilusa
Name:		nautilus-dropbox
Version:	0.4.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.getdropbox.com/u/5143/nautilus-dropbox-packages/%{version}/%{name}-%{version}.tar.bz2
URL:		http://getdropbox.com/
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2.12.0
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	nautilus-devel >= 2.20.0
BuildRequires:	pkgconfig
Requires(post,postun):	hicolor-icon-theme
Requires:	nautilus >= 2.16.0
Requires:	wget >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dropbox extension for Nautilus used as sync, versioning and backup
software for your local and remote resources between a number of
machines.

%description -l pl.UTF-8
Rozszerzenie Dropbox dla Nautilusa używane do synchronizacji, obsługi
wersji oraz tworzenia kopii zapasowych zasobów lokalnych oraz zdalnych
pomiędzy określonymi maszynami.

%prep
%setup -q

%build
%configure \
	--disable-dependency-tracking \
	--enable-static=no \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-dropbox.so
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/emblems/*.icon
