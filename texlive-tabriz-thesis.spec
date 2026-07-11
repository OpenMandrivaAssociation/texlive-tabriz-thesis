%global tl_name tabriz-thesis
%global tl_revision 51729

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A template for the University of Tabriz
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/tabriz-thesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabriz-thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabriz-thesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a document class for typesetting theses and
dissertations at the University of Tabriz. The class requires use of
XeLaTeX.

