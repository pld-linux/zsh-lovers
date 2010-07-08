Summary:	zsh-lovers is a small project which tries to collect tips, tricks and examples for the Z shell
Summary(hu.UTF-8):	zsh-lovers egy kis project, amely megpróbálja összegyűjteni a tippeket, trükköket és példákat a Z shell-hez
Name:		zsh-lovers
Version:	0.8.3
Release:	1
License:	GPL v2
Group:		Documentation
Source0:	http://deb.grml.org/pool/main/z/zsh-lovers/%{name}_%{version}.tar.gz
# Source0-md5:	6604f3bb8a971e66281e1369cc4bd033
Source1:	http://grml.org/zsh/%{name}.1
# Source1-md5:	d7b586ffa91bb63356ed0080699cef93
URL:		http://grml.org/zsh/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zsh-lovers is a small project which tries to collect tips, tricks and
examples for the Z shell.

%description  -l hu.UTF-8
zsh-lovers egy kis project, amely megpróbálja összegyűjteni a
tippeket, trükköket és példákat a Z shell-hez.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

cp -rf README refcard.pdf  zsh-lovers.1.txt  zsh_people $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man1/zsh-lovers.1*
