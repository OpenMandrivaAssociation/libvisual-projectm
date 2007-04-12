%define name libvisual-projectm
%define version 0.99
%define release %mkrel 1
%define oname libvisual-projectM
%define major 0
%define libname %mklibname projectm %major

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
BuildRequires: libprojectm-devel

%description
projectM is a reimplementation of Milkdrop under OpenGL.

%package data
Summary: Visualization library for OpenGL based on Milkdrop 
Group: Graphics

%description data
projectM is a reimplementation of Milkdrop under OpenGL. This contains data
files and presets.

%package -n %libname
Summary: Visualization library for OpenGL based on Milkdrop
Group: System/Libraries
Requires: %name-data >= %version

%description -n %libname
projectM is a reimplementation of Milkdrop under OpenGL.

%package -n %libname-devel
Summary: Visualization library for OpenGL based on Milkdrop
Group: Development/C
Requires: %libname = %version
Provides: libprojectm-devel = %version-%release

%description -n %libname-devel
projectM is a reimplementation of Milkdrop under OpenGL.


%prep
%setup -q -n %oname
aclocal -I m4
autoconf
automake

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%dir %_libdir/libvisual-0.4/
%dir %_libdir/libvisual-0.4/actor/
%_libdir/libvisual-0.4/actor/actor_projectM.so
%_libdir/libvisual-0.4/actor/actor_projectM.la


