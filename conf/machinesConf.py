

machinesConf = [
  # Grow room
  {
    'name': 'Growing room',
    'enabled': True,
    'pins' :{
        'fan_extraction':19,
        'fan_intraction': False,
        'fan_room': False,
        'lamp':5,
        'pump': False #17
    },
    'timer': {'day': '18:00', 'night':'14:00'}
  },
  # Flowering room
  {
    'name': 'Flowering room',
    'enabled': False,
    'pins' :{
        'fan_extraction':False,
        'fan_intraction': False,
        'fan_room': False,
        'lamp':27,
        'pump': False # 22
    },
    'timer': {'day': '18:00', 'night':'14:00'}
  }
]
