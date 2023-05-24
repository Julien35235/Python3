from dominate import document
from dominate.tags import *

bios_infos = [
    {
        'title': 'EFI',
        'description': 'EFI (Extensible Firmware Interface) est une norme plus récente pour initialiser et démarrer les ordinateurs.',
        'image': 'https://www.intel.com/content/dam/www/public/us/en/images/illustrations/efi-overview-illustration-v3.png'
    },
    {
        'title': 'UEFI',
        'description': 'UEFI (Unified Extensible Firmware Interface) est une version plus récente d\'EFI qui offre des fonctionnalités et une sécurité plus avancées.',
        'image': 'https://www.techgenix.com/wp-content/uploads/2018/08/UEFI-image.png'
    }
]

doc = document(title='Informations sur les BIOS en EFI et UEFI')

with doc.add(section()):
    h1('Informations sur les BIOS en EFI et UEFI')

    i = 0
    while i < len(bios_infos):
        with div():
            with div():
                img(src=bios_infos[i]['image'], alt=bios_infos[i]['title'])
            with div():
                h2(bios_infos[i]['title'])
                p(bios_infos[i]['description'])
        i += 1

doc.save('bios.html')
