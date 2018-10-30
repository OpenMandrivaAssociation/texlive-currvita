# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/currvita
# catalog-date 2006-12-09 16:04:04 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-currvita
Version:	20180303
Release:	2
Summary:	Typeset a curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/currvita
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currvita.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currvita.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currvita.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Currvita is a package rather than a class (like most other
curriculum vitae offerings). The author considers that a
curriculum vitae can quite reasonably form part of another
document (such as a letter, or a dissertation).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/currvita/currvita.sty
%doc %{_texmfdistdir}/doc/latex/currvita/README
%doc %{_texmfdistdir}/doc/latex/currvita/currvita.pdf
%doc %{_texmfdistdir}/doc/latex/currvita/cvtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/currvita/currvita.dtx
%doc %{_texmfdistdir}/source/latex/currvita/currvita.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061209-2
+ Revision: 750749
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061209-1
+ Revision: 718186
- texlive-currvita
- texlive-currvita
- texlive-currvita
- texlive-currvita

