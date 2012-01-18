Summary:	Dropbox extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Dropbox dla Nautilusa
Name:		nautilus-dropbox
Version:	0.7.1
Release:	1
License:	GPL v2 with exceptions
Group:		X11/Applications
Source0:	http://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	f08f6ffaecea55c2f1e615876dbf9479
Patch0:		dropboxd-path.patch
URL:		http://getdropbox.com/
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	python-docutils
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	nautilus >= 3.0.0
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
%patch0 -p1

%build
%configure \
	--disable-dependency-tracking \
	--enable-static=no \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dropbox
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-dropbox.so
%{_iconsdir}/hicolor/*/*/*.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/emblems
%{_datadir}/%{name}/emblems/*.icon
%{_datadir}/%{name}/emblems/*.png
%{_desktopdir}/dropbox.desktop
%{_mandir}/man1/*.1*
