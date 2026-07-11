%global tl_name tqft
%global tl_revision 71401

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Drawing TQFT diagrams with TikZ/PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tqft
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tqft.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tqft.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tqft.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines some node shapes useful for drawing TQFT diagrams
with TikZ/PGF. That is, it defines highly customisable shapes that look
like cobordisms between circles, such as those used in TQFT and other
mathematical diagrams.

