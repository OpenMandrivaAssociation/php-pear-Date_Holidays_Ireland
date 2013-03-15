%define		_class		Date
%define		_subclass	Holidays
%define		_region		Ireland
%define		upstream_name	%{_class}_%{_subclass}_%{_region}

Name:		php-pear-%{upstream_name}
Version:	0.1.3
Release:	3
Summary:	Driver based class to calculate holidays in %{_region}
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.21.1
BuildArch:	noarch
BuildRequires:	php-pear

%description
%{upstream_name} is the Date_Holidays driver for %{_region} region.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed Jan 25 2012 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-1mdv2012.0
+ Revision: 768664
- import php-pear-Date_Holidays_Ireland


