%define upstream_name    Msgcat
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 6

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-6mdv2012.0
+ Revision: 765497
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-5
+ Revision: 763992
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-4
+ Revision: 667266
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.30.0-3mdv2011.0
+ Revision: 564548
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 556011
- rebuild for perl 5.12

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 407810
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.03-20mdv2009.0
+ Revision: 223846
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.03-19mdv2008.1
+ Revision: 152213
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.03-18mdv2008.0
+ Revision: 23336
- rebuild


* Mon May 01 2006 Stefan van der Eijk <stefan@eijk.nu> 1.03-17mdk
-_rebuild_for_sparc

* Thu Nov 18 2004 Michael Scherer <misc@mandrake.org> 1.03-16mdk
- Rebuild for new perl

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.03-15mdk
- Own dir

* Thu Aug 14 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 1.03-14mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.03-13mdk
- rebuild for new auto{prov,req}

