%global php_apiver %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)

%define real_name php-magickwand
%define php_base php52

Summary:	PHP API for ImageMagick
Name:		%{php_base}-magickwand
Version:	0.1.9
Release:	3.ius%{?dist}
License:	ImageMagick
Group:		Development/Languages
Source0:	ftp://ftp.wl.sggw.pl/outgoing/graphics/ImageMagick/magickwand-%{version}.tar.gz
Source1:	magickwand.ini
Patch:		php-magickwand-0.1.9-abi.patch
URL:		http://www.magickwand.org
BuildRequires:  ImageMagick-devel >= 6.2.4.1, 
BuildRequires:	autoconf, automake, libtool
BuildRequires:	%{php_base}-devel >= 4.3.0, 
Requires:	%{php_base}-api = %{php_apiver}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides: 	%{real_name} = %{version}-%{release}

%description
MagickWand for PHP is a native PHP interface to the new
ImageMagick MagickWand API. It is an almost complete port
of the ImageMagick C API, excluding some X-Server related
functionality and progress monitoring.

%prep
%setup -q -n magickwand
%patch -p1 -b .abi
export PHP_RPATH=no
phpize
%configure

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install-modules INSTALL_ROOT=$RPM_BUILD_ROOT
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/php.d/magickwand.ini

# Fix incorrect end-of-line encoding
sed -i 's/\r//' README

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHOR ChangeLog CREDITS LICENSE README TODO
%{_libdir}/php/modules/magickwand.so
%config(noreplace) %{_sysconfdir}/php.d/magickwand.ini

%changelog
* Thu Mar 31 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> 0.1.9-3
- Porting from EPEL to IUS for php52 and php53u

* Mon Apr 28 2008 Robert Scheck <robert@fedoraproject.org> 0.1.9-2
- Work around missing MagickRecolorImage ABI (#443193)

* Fri Dec 28 2007 Robert Scheck <robert@fedoraproject.org> 0.1.9-1
- Upgrade to 0.1.9

* Wed Aug 29 2007 Robert Scheck <robert@fedoraproject.org> 0.1.8-4
- Updated the license tag according to the guidelines

* Sun Sep 03 2006 Robert Scheck <robert@fedoraproject.org> 0.1.8-3
- Rebuild for Fedora Core 6

* Sat Jun 17 2006 Robert Scheck <robert@fedoraproject.org> 0.1.8-2
- Changes to match with Fedora Packaging Guidelines (#194470)

* Mon May 29 2006 Robert Scheck <robert@fedoraproject.org> 0.1.8-1
- Upgrade to 0.1.8
- Initial spec file for Fedora Core
