Summary:	Parallel tar, rm and cp utilities
Name:		fss-parallel-tools
Version:	1.49
Release:	1
License:	UPL v1.0
Group:		Applications/Archiving
Source0:	https://yum.oracle.com/repo/OracleLinux/OL6/developer/x86_64/getPackageSource/%{name}-%{version}-1.el6.src.rpm
# Source0-md5:	eaa350bba272e14bae733b3b9d72da46
Patch0:		build.patch
URL:		https://blogs.oracle.com/cloud-infrastructure/announcing-parallel-file-tools-for-file-storage
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parallel tar, rm and cp utilities

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -dim
tar xf *.tar.gz
cd %{name}
%patch0 -p1

%build
%{__make} -C %{name} \
	CC="%{__cc}" \
	GCOV_FLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cp -p parcp parrm partar $RPM_BUILD_ROOT%{_bindir}
cp -p *.1* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/parcp
%attr(755,root,root) %{_bindir}/parrm
%attr(755,root,root) %{_bindir}/partar
%{_mandir}/man1/parcp.1*
%{_mandir}/man1/parrm.1*
%{_mandir}/man1/partar.1*
