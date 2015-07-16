Summary: UUID VMOD for Varnish
Name: vmod-varnish-%{VARNISHVER}-uuid
Version: 0.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: libvmod-uuid.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 4.0
BuildRequires: make, python-docutils

%description
UUID VMOD

%prep
%setup -n libvmod-uuid

%build
./configure --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
make
make check

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}/
cp README.rst %{buildroot}/usr/share/doc/%{name}/
cp LICENSE %{buildroot}/usr/share/doc/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.
