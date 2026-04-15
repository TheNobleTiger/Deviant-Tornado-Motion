cm1runs is the directory of cm1 runs. currently inside you will find the following:
 - Default Runs (This is based purely on the standard cm1 runs with no changes made after compiling)
 - elreno (This is simulating using a sounding sourced from the May 31 2013 El Reno tornadic event)

.gitattributes:
 - This is to filter out .nc files, our runs are too large to do a standard push. I have to utilize git lfs.

cm1visualizer.py:
 - This python script is being developed to simulate various different products from the CM1 model, the goal is for variables at the top to be enabled true or false. Using if statements the program then will plot the specefied items (or save the outputs as pngs in a folder you name). The program has been well commented, my goal is that someone who has never read code could take a look at the file at any line and understand what is going on (the what and why).

radarscope-br.pal/radarscopeBR_raw.pal:
 - Rather than use a standard color map I wanted to incorporate the visuals of radarscopes expert color palette, this was something I worked on previously with my mentor as a fun coding challenge. I wanted to utilize this again but I also provided the raw file if you wanted to reverse engineer what I have done.

_____________________________________________________________________________________________________________________

Variables:

File: /elreno/cm1out_000007.nc

  ztop             shape=(1,)                     dims=('one',)  km  height at top of model
  time             shape=(1,)                     dims=('time',)  seconds  time since beginning of simulation
  xh               shape=(300,)                   dims=('xh',)  km  west-east location of scalar grid points
  xf               shape=(301,)                   dims=('xf',)  km  west-east location of staggered u grid points
  yh               shape=(300,)                   dims=('yh',)  km  south-north location of scalar grid points
  yf               shape=(301,)                   dims=('yf',)  km  south-north location of staggered v grid points
  zh               shape=(50,)                    dims=('zh',)  km  nominal height of scalar grid points
  zf               shape=(51,)                    dims=('zf',)  km  nominal height of staggered w grid points
  umove            shape=(1,)                     dims=('time',)  m/s  umove
  vmove            shape=(1,)                     dims=('time',)  m/s  vmove
  rain             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  cm  accumulated surface rainfall
  prate            shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  kg/m2/s  surface precipitation rate
  sws              shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  m/s  max horiz wind speed at lowest model level
  svs              shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  1/s  max vert vorticity at lowest model level
  sps              shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  Pa  min pressure at lowest model level
  srs              shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  kg/kg  max qr at lowest model level
  sgs              shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  kg/kg  max qg at lowest model level
  sus              shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  m/s  max w at 5 km AGL
  shs              shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  m2/s2  max integrated updraft helicity
  rain2            shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  cm  translated surface rainfall
  sws2             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  m/s  translated max horiz wspd at lowest model level
  svs2             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  1/s  translated max vert vort at lowest model level
  sps2             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  Pa  translated min pressure at lowest model level
  srs2             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  kg/kg  translated max qr at lowest model level
  sgs2             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  kg/kg  translated max qg at lowest model level
  sus2             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  m/s  translated max w at 5 km AGL
  shs2             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  m2/s2  translated max integrated updraft helicity
  cref             shape=(1, 300, 300)            dims=('time', 'yh', 'xh')  dBZ  composite reflectivity
  th               shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  K  potential temperature
  prs              shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  Pa  pressure
  qv               shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  kg/kg  water vapor mixing ratio
  qc               shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  kg/kg  qc
  qr               shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  kg/kg  qr
  qi               shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  kg/kg  qi
  qs               shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  kg/kg  qs
  qg               shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  kg/kg  qg
  nci              shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  #/kg  nci
  ncs              shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  #/kg  ncs
  ncr              shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  #/kg  ncr
  ncg              shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  #/kg  ncg
  dbz              shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  dBZ  reflectivity
  uinterp          shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  m/s  u interpolated to scalar points (grid-relative)
  vinterp          shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  m/s  v interpolated to scalar points (grid-relative)
  winterp          shape=(1, 50, 300, 300)        dims=('time', 'zh', 'yh', 'xh')  m/s  w interpolated to scalar points
  u                shape=(1, 50, 300, 301)        dims=('time', 'zh', 'yh', 'xf')  m/s  E-W (x) velocity (grid-relative)
  v                shape=(1, 50, 301, 300)        dims=('time', 'zh', 'yf', 'xh')  m/s  N-S (y) velocity (grid-relative)
  w                shape=(1, 51, 300, 300)        dims=('time', 'zf', 'yh', 'xh')  m/s  vertical velocity
  tke              shape=(1, 51, 300, 300)        dims=('time', 'zf', 'yh', 'xh')  m^2/s^2  subgrid turbulence kinetic energy
  kmh              shape=(1, 51, 300, 300)        dims=('time', 'zf', 'yh', 'xh')  m^2/s  horizontal eddy viscosity for momentum
  kmv              shape=(1, 51, 300, 300)        dims=('time', 'zf', 'yh', 'xh')  m^2/s  vertical eddy viscosity for momentum
  khh              shape=(1, 51, 300, 300)        dims=('time', 'zf', 'yh', 'xh')  m^2/s  horizontal eddy diffusivity for scalars
  khv              shape=(1, 51, 300, 300)        dims=('time', 'zf', 'yh', 'xh')  m^2/s  vertical eddy diffusivity for scalars
