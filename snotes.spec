# TODO: optflags
%define		ver	1.1.4-2
%define		_ver	%(echo %ver | tr - _)
Summary:	Sticky little notes on desktop
Summary(pl.UTF-8):   Notatki przyklejane na pulpicie
Name:		snotes
Version:	%{_ver}
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/s-notes/%{name}-%{ver}.tar.gz
# Source0-md5:	b49a9639cf479b4a22947676344f58e9
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sticky little notes on desktop.

%description -l pl.UTF-8
Notatki przyklejane na pulpicie.

%prep
%setup -q -n %{name}

%build
rm -f snotes *.o
qmake -project
qmake -nocache
%{__sed} -i -e s/-lqt/-lqt-mt/ Makefile
%{__make} \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

install -D snotes $RPM_BUILD_ROOT%{_bindir}/snotes
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
