Name:		texlive-tabriz-thesis
Version:	51729
Release:	2
Summary:	A template for the University of Tabriz
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabriz-thesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabriz-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabriz-thesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a document class for typesetting theses and
dissertations at the University of Tabriz.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabriz-thesis
%{_texmfdistdir}/tex/xelatex/tabriz-thesis
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis
%doc %{_texmfdistdir}/doc/xelatex/tabriz-thesis

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
