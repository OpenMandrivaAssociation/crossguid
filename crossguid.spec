%define git 20150804

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Lightweight cross platform C++ GUID/UUID library
Name:		crossguid
Version:	0
Release:	0.%{git}.1
License:	MIT
Group:		System/Libraries
Url:		https://github.com/graeme-hill/crossguid
Source0:	%{name}-%{git}.tar.bz2
Source1:	Makefile.crossguid
BuildRequires:	pkgconfig(uuid)

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and had a generic class
for parsing, stringifying, and comparing IDs.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for lightweight cross platform C++ GUID/UUID library
Group:		System/Libraries

%description -n %{libname}
Shared library for lightweight cross platform C++ GUID/UUID library.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for lightweight cross platform C++ GUID/UUID library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for lightweight cross platform C++ GUID/UUID library.

%files -n %{devname}
%{_includedir}/guid.h
%{_libdir}/lib%{name}.so

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{git}
cp %{SOURCE1} Makefile

%build
%setup_compile_flags
%make

%install
%makeinstall_std \
	LIBDIR=%{_libdir}


%changelog

* Mon Feb 22 2016 Rosa <rosa@abf.rosalinux.ru> 0-0.20150804.1
- (bf2e817) Automatic import for version 0-0.20150804.1


