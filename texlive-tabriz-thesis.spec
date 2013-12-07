# revision 29421
# category Package
# catalog-ctan /macros/latex/contrib/tabriz-thesis
# catalog-date 2013-03-17 16:41:59 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-tabriz-thesis
Version:	1.1
Release:	3
Summary:	A template for the University of Tabriz
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabriz-thesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabriz-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabriz-thesis.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/tabriz-thesis/tabriz-thesis.cls
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/README
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/appendix1.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/chapter1.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/chapter2.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/chapter3.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/dicen2fa.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/dicfa2en.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/en-title.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/fa-title.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/logo.jpg
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/references.tex
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/tabriz-thesis.pdf
%doc %{_texmfdistdir}/doc/latex/tabriz-thesis/tabriz-thesis.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
