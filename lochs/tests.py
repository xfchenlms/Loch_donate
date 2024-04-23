from django.test import TestCase
from unittest.mock import patch
from .models import Loch

from django.urls import reverse
from .models import Loch, CartItem
class LochsAppTests(TestCase):
    @patch('lochs.models.Loch.objects.get')
    def test_surface_area(self, mock_get):
      
        loch = Loch()
        loch.SurfaceArea = 100.0
      
        mock_get.return_value = loch

      
        surface_area = loch.SurfaceArea
      
        self.assertEqual(surface_area, 100.0)

def test_add_to_cart(self):
    
        response = self.client.post(reverse('add_to_cart', args=[self.loch.id]))
        
   
        self.assertEqual(response.status_code, 302)
        
      
        self.assertTrue(CartItem.objects.exists())