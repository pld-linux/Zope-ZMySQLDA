%define zope_subname ZMySQLDA
Summary:	Zope MySQL database adapter
Summary(pl):	Interfejs bazy danych MySQL do Zope
Name:		Zope-%{zope_subname}
Version:	2.0.8
Release:	4
License:	ZPL
Group:		Development/Languages/Python
Source0:	http://www.zope.org/Members/adustman/Products/ZMySQLDA/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	74332272e53b13c6b19d3185d575699c
URL:		http://www.zope.org/Members/adustman/Products/ZMySQLDA/
BuildRequires:  python
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	python-MySQLdb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zope MySQL database adapter.

%description -l pl
Interfejs bazy danych MySQL do Zope.

%prep
%setup -q -c
mv -f lib/python/Products/%{zope_subname}/* .
rm -rf lib

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af *.py *.dtml help icons $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname} 
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/%{name}
