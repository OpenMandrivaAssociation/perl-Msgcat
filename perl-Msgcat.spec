%define upstream_name    Msgcat
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Msgcat, a small Perl module for XPG4 message catalog functions
License:    GPL
Group:      Development/Perl
Url:        http://www.cpan.org
Source0:    ftp://ftp.pasteur.fr/pub/computing/CPAN/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is Msgcat, a small Perl modules for systems which support the XPG4 message
catalog functions : catopen(3), catgets(3) and catclose(4).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# for docs files (fpons)
chmod 0644 README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
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
