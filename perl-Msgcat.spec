%define name perl-Msgcat
%define real_name Msgcat
%define version 1.03
%define release 17mdk

Summary: Msgcat, a small Perl module for XPG4 message catalog functions
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Perl
URL: http://www.cpan.org
Source: ftp://ftp.pasteur.fr/pub/computing/CPAN/modules/by-module/Locale/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
Buildroot: %{_tmppath}/%{name}-root

%description
This is Msgcat, a small Perl modules for systems which support the XPG4 message
catalog functions : catopen(3), catgets(3) and catclose(4).

%prep
%setup -q -n %{real_name}-%{version}

# for docs files (fpons)
chmod 0644 README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale

