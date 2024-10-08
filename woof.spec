Name:           woof
Version:        14.5.0
Release:        %autorelease
Summary:        A continuation of the MBF source port for modern systems

License:        GPLv2+
URL:            https://github.com/fabiangreffrath/woof
Source0:        https://github.com/fabiangreffrath/woof/archive/refs/tags/woof_14.5.0.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  openal-soft-devel
BuildRequires:  libsndfile-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  libxmp-devel
Requires:       SDL2
Requires:       SDL2_net
Requires:       openal-soft
Requires:       libsndfile
Requires:       fluidsynth
Requires:       libxmp

%description
MBF stands for "Marine's Best Friend" and is widely regarded as the successor of the Boom source port by TeamTNT. It serves as the code base for popular Doom source ports such as PrBoom+/DSDA-Doom or The Eternity Engine. As the original engine was limited to run only under MS-DOS, it has been ported to Windows by Team Eternity under the name WinMBF in 2004. Woof! is developed based on the WinMBF code with the aim to make MBF more widely available and convenient to use on modern systems.

To achieve this goal, this source port is less strict regarding its faithfulness to the original MBF. It is focused on quality-of-life enhancements, bug fixes and compatibility improvements. However, all changes have been introduced in good faith that they are in line with the original author's intentions and even for the trained eye, this source port should still look very familiar to the original MBF.

In summary, this project's goal is to fast-forward MBF.EXE from DOS to 21st century and remove all the stumbling blocks on the way. Furthermore, just as MBF was ahead of its time, this project dedicates itself to early adoption of new modding features such as DEHEXTRA+DSDHacked, UMAPINFO and MBF21.

%prep
%setup -n woof-woof_14.5.0

%build
%cmake -B build -DCMAKE_BUILD_TYPE=Release
make -C build %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install -C build

%files
%{_bindir}/woof
%{_bindir}/woof-setup
%{_datadir}/*

%changelog
* Tue Oct 08 2024 Danilo Soares <deudzdev@gmail.com> - 14.5.0
- Bump version to 14.5.0

* Sun Mar 10 2024 Danilo Soares <deudzdev@gmail.com> - 14.2.0
- Initial release
