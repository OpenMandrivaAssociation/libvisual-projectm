%define name libvisual-projectm
%define version 2.0.1
%define release 3
%define oname projectM_libvisual

Summary: Visualization module for libvisual based on projectM
Name: %{name}
Version: %{version}
Release:	1
#new source file, from http://sourceforge.net/projects/projectm/files/2.1.0/
Source0: http://downloads.sourceforge.net/project/projectm/2.1.0/%{oname}-%{version}-Source.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: https://xmms-projectm.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pkgconfig(libvisual-0.4)
BuildRequires: libprojectm-devel >= 1:2.0
BuildRequires: pkgconfig(sdl)
BuildRequires: cmake

%description
projectM is a reimplementation of Milkdrop under OpenGL.

%package data
Summary: Visualization library for OpenGL based on Milkdrop 
Group: Graphics

%description data
projectM is a reimplementation of Milkdrop under OpenGL. This contains data
files and presets.


%prep
%setup -q -n %oname-%version-Source

%build
cmake . -DCMAKE_INSTALL_PREFIX=%_prefix
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%dir %_libdir/libvisual-0.4/
%dir %_libdir/libvisual-0.4/actor/
%_libdir/libvisual-0.4/actor/libprojectM_libvisual.so

