%define modname	Msgcat
%define modver	1.03

Summary:	Msgcat, a small Perl module for XPG4 message catalog functions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.pasteur.fr/pub/computing/CPAN/modules/by-module/Locale/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel

%description
This is Msgcat, a small Perl modules for systems which support the XPG4 message
catalog functions :	catopen(3), catgets(3) and catclose(4).

%prep
%setup -qn %{modname}-%{modver}

# for docs files (fpons)
chmod 0644 README Changes

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/man3/*

