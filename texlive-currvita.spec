Name:		texlive-currvita
Version:	15878
Release:	1
Summary:	Typeset a curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/currvita
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currvita.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currvita.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currvita.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
