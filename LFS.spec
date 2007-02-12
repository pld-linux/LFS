Summary:	LDP Linux From Scratch
Summary(pl.UTF-8):   LDP - Linux od podstaw
Name:		LFS
Version:	3.3
Release:	2
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/lfs/%{name}.html.tar.gz
# Source0-md5:	b4aa81ba612bbb0ca0ec86bb17229145
URL:		http://www.tldp.org/LDP/lfs/LFS/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Derived from the popular Linux-From-Scratch-HOWTO, this book describes
the process of creating your own Linux system from scratch from an
already installed Linux distribution, using nothing but the sources of
software that are needed.

More information can be found at http://linuxfromscratch.org/.

%description -l pl.UTF-8
Ten dokument wywodzi się z Linux-From-Scratch-HOWTO, opisuje proces
tworzenia własnego systemu linuksowego bazując na zainstalowanej już
dystrybucji Linuksa, używając jedynie źródeł potrzebnych programów.

Więcej informacji na stronie http://linuxfromscratch.org/.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
