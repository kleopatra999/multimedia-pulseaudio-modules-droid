%define device sbj
%define pulseversion 2.1

Name:       pulseaudio-modules-droid-%{device}

Summary:    PulseAudio Droid HAL modules
Version:    %{pulseversion}.0
Release:    1
Group:      Multimedia/PulseAudio
License:    LGPLv2.1+
URL:        https://github.com/nemomobile/pulseaudio-modules-nemo
Source0:    %{name}-%{version}.tar.bz2
Source1:    pulseaudio-modules-droid.spec.in
Source2:    precheckin.sh
Requires:   pulseaudio >= 2.1
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pkgconfig(pulsecore) >= 2.1
BuildRequires:  pkgconfig(android-headers)
BuildRequires:  pkgconfig(libhardware)
Provides: pulseaudio-modules-droid

%description
PulseAudio Droid HAL modules.


%prep
%setup -q -n %{name}-%{version}

%build
%reconfigure --disable-static --with-droid-device=%{device}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/*.so
