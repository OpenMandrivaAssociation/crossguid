%define major 0
%define oldlibname %mklibname %{name} %{major}
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	Lightweight cross platform C++ GUID/UUID library
Name:		crossguid
Version:	0.2.3~20190529
Release:	1
License:	MIT
Group:		System/Libraries
Url:		https://github.com/graeme-hill/crossguid
Source0:	https://github.com/graeme-hill/crossguid/archive/refs/heads/master.tar.gz
BuildSystem:	cmake
BuildRequires:	pkgconfig(uuid)

%patchlist
crossguid-shared.patch

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and had a generic class
for parsing, stringifying, and comparing IDs.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for lightweight cross platform C++ GUID/UUID library
Group:		System/Libraries
# Renamed before OM 6.0 2025/04/12
%rename %{oldlibname}

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
%{_includedir}/crossguid
%{_includedir}/guid.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/crossguid.pc
%{_datadir}/crossguid

%install -a
# For compatibility with Makefile from previous version
ln -s crossguid/guid.hpp %{buildroot}%{_includedir}/guid.h
