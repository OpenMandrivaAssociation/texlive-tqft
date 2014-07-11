# revision 33411
# category Package
# catalog-ctan /macros/latex/contrib/tqft
# catalog-date 2014-04-08 15:56:54 +0200
# catalog-license lppl1.3
# catalog-version 2.0
Name:		texlive-tqft
Version:	2.0
Release:	2
Summary:	Drawing TQFT diagrams with TikZ/PGF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tqft
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tqft.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tqft.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tqft.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines some node shapes useful for drawing TQFT
diagrams with TikZ/PGF. That is, it defines highly customisable
shapes that look like cobordisms between circles, such as those
used in TQFT and other mathematical diagrams.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tqft/tikzlibrarytqft.code.tex
%{_texmfdistdir}/tex/latex/tqft/tqft.sty
%doc %{_texmfdistdir}/doc/latex/tqft/README
%doc %{_texmfdistdir}/doc/latex/tqft/tqft_doc.pdf
%doc %{_texmfdistdir}/doc/latex/tqft/tqft_doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/tqft/tqft.dtx
%doc %{_texmfdistdir}/source/latex/tqft/tqft.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
