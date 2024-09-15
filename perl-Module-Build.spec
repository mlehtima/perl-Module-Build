%global cpan_version_major 0.42
%global cpan_version_minor 08
%global cpan_version %{cpan_version_major}%{?cpan_version_minor}

Name:           perl-Module-Build
Epoch:          1
Version:        %{cpan_version_major}%{?cpan_version_minor:.%cpan_version_minor}
Release:        1
Summary:        Build and install Perl modules
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Module-Build/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Module-Build-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
#BuildRequires:  perl(CPAN::Meta) >= 2.110420
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.003
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
%if 0%(perl -e 'print $] > 5.019')
BuildRequires:  perl(deprecate)
%endif
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::Install) >= 0.3
BuildRequires:  perl(ExtUtils::Installed)
BuildRequires:  perl(ExtUtils::Manifest) >= 1.54
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::Packlist)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
#BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.15
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
# perl(Module::Build) is loaded from ./lib
BuildRequires:  perl(Module::Metadata) >= 1.000002
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4401
BuildRequires:  perl(Perl::OSType) >= 1
BuildRequires:  perl(strict)
# Optional tests:
#%if !%{defined perl_bootstrap}
#BuildRequires:  perl(Archive::Zip)
#BuildRequires:  perl(PAR::Dist)
#%if 0%{?fedora}  || 0%{?rhel} < 7
#BuildRequires:  perl(Pod::Readme)
#%endif
#%endif
BuildRequires:  perl(Test::Harness) >= 3.16
BuildRequires:  perl(Test::More) >= 0.49
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version) >= 0.87
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
#Requires:       perl(CPAN::Meta) >= 2.110420
Requires:       perl(ExtUtils::CBuilder) >= 0.27
Requires:       perl(ExtUtils::Install) >= 0.3
Requires:       perl(ExtUtils::Manifest) >= 1.54
Requires:       perl(ExtUtils::Mkbootstrap)
Requires:       perl(ExtUtils::ParseXS) >= 2.21
Requires:       perl(Module::Metadata) >= 1.000002
# Keep PAR support optional (PAR::Dist)
Requires:       perl(Perl::OSType) >= 1
Requires:       perl(Test::Harness)
# Optional run-time needed for generating documentation from POD:
Requires:       perl(Pod::Html)
Requires:       perl(Pod::Man) >= 2.17
Requires:       perl(Pod::Text)
# Run-time for generated Build scripts from Build.PLs:
# Those are already found by dependency generator. Just make sure they
# present.
# Cwd
# File::Basename
# File::Spec
# strict

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((ExtUtils::Install|File::Spec|Module::Build|Module::Metadata|Perl::OSType)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::YAML\\) >= 0.002$

%description
Module::Build is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to ExtUtils::MakeMaker.
Developers may alter the behavior of the module through sub-classing in a
much more straightforward way than with MakeMaker. It also does not require
a make on your system - most of the Module::Build code is pure-perl and
written in a very cross-platform way. In fact, you don't even need a shell,
so even platforms like MacOS (traditional) can use it fairly easily. Its
only prerequisites are modules that are included with perl 5.6.0, and it
works fine on perl 5.005 if you can install a few additional modules.

%prep
%setup -q -n Module-Build-%{cpan_version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
#pushd Module-Build-0.4208
#rm t/signature.t
#LANG=C TEST_SIGNATURE=1 MB_TEST_EXPERIMENTAL=1 ./Build test
#popd

%files
%doc Changes contrib LICENSE README
%{_bindir}/config_data
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
