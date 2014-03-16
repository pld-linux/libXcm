#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	X Color Management library
Summary(pl.UTF-8):	Biblioteka X Color Management (zarządzanie kolorami w X)
Name:		libXcm
Version:	0.5.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/oyranos/%{name}-%{version}.tar.bz2
# Source0-md5:	c5d293b235f98f0bd211678ffefebc4c
Patch0:		%{name}-link.patch
URL:		http://www.oyranos.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libXcm library contains the a reference implementation of the X
Color Management specification. The X Color Management specification 
allows to attach color regions to X windows to communicate with
color servers.

%description -l pl.UTF-8
Biblioteka libXcm zawiera wzorcową implementację specyfikacji X Color
Management. Specyfikacja ta pozwala na dołączanie regionów kolorów do
okien X w celu komunikacji z serwerami kolorów.

%package devel
Summary:	Header files for libXcm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXcm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-proto-xproto-devel

%description devel
Header files for libXcm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libXcm.

%package static
Summary:	Static libXcm library
Summary(pl.UTF-8):	Statyczna biblioteka libXcm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libXcm library.

%description static -l pl.UTF-8
Statyczna biblioteka libXcm.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXcm*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README docs/X_Color_Management.txt
%attr(755,root,root) %{_libdir}/libXcm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXcm.so.0
%attr(755,root,root) %{_libdir}/libXcmDDC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXcmDDC.so.0
%attr(755,root,root) %{_libdir}/libXcmEDID.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXcmEDID.so.0
%attr(755,root,root) %{_libdir}/libXcmX11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXcmX11.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcm.so
%attr(755,root,root) %{_libdir}/libXcmDDC.so
%attr(755,root,root) %{_libdir}/libXcmEDID.so
%attr(755,root,root) %{_libdir}/libXcmX11.so
%{_includedir}/X11/Xcm
%{_pkgconfigdir}/xcm.pc
%{_pkgconfigdir}/xcm-ddc.pc
%{_pkgconfigdir}/xcm-edid.pc
%{_pkgconfigdir}/xcm-x11.pc
%{_libdir}/cmake/Xcm
%{_mandir}/man3/Xcm*.3*
%{_mandir}/man3/Xcolor*.3*
%{_mandir}/man3/libXcm.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libXcm.a
%{_libdir}/libXcmDDC.a
%{_libdir}/libXcmEDID.a
%{_libdir}/libXcmX11.a
%endif
