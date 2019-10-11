Name:		fasttext
Version:	0.9.1
Release:	1%{?dist}
Summary:	Efficient learning of word representations and sentence classification

License:	MIT
URL:		https://github.com/facebookresearch/fastText
Source0:	https://github.com/facebookresearch/fastText/archive/v%{version}/%{name}-%{version}.tar.gz
# Enable soversion explicitly to avoid unintentional soname bump
Patch0:		enable-soversion.patch
# Enable pkg-config feature for users of libfasttext-devel package
Patch1:		enable-pkg-config.patch
# Enable to install %%{_libdir} instead of hardcoded lib directory
Patch2:		enable-install-lib64.patch
# Respect CMake CXXFLAGS set by %%cmake (Needed for hardening with -fPIC)
Patch3:		respect-cmake-cxxflags.patch

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
Requires:	%{name}-libs = %{version}-%{release}

%description
The fastText is a library for efficient learning of
word representations and sentence classification.

%package libs
Summary:	Runtime libraries for fastText

%description libs
This package contains the libraries for fastText.

%package tools
Summary:	Tools for fastText
Requires:	%{name}-libs = %{version}-%{release}

%description tools
This package contains tools for manipulate models for fastText.

%package devel
Summary:	Libraries and header files for fastText
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains header files to develop a software using fastText.

%prep
%autosetup -p1 -n fastText-%{version}

%build
export CXXFLAGS="%build_cxxflags -fPIC"
%cmake .
%make_build V=1

%install
%make_install
find %{buildroot}%{_libdir} -name '*.a' -delete

%files 
%{_bindir}/fasttext

%files libs
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_libdir}/libfasttext.so.0

%files devel
%dir %{_includedir}/fasttext
%{_includedir}/fasttext/
%{_libdir}/libfasttext.so
%{_libdir}/pkgconfig/fasttext.pc

%changelog
* Tue Oct 1 2019 Kentaro Hayashi <hayashi@clear-code.com> - 0.9.1-1
- initial packaging
