%define name libvisual-projectm
%define version 1.0
%define release %mkrel 1
%define oname projectM-libvisual

Summary: Visualization module for libvisual based on projectM
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://xmms-projectm.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libvisual-devel
BuildRequires: libprojectm-devel >= 1.0
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
%setup -q -n %oname-%version

%build
cmake . -DCMAKE_INSTALL_PREFIX=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%dir %_libdir/libvisual-0.4/
%dir %_libdir/libvisual-0.4/actor/
%_libdir/libvisual-0.4/actor/libprojectM_libvisual.so


