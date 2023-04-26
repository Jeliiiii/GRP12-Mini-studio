from Shared.Actors.operatorWindows.PseudoWindow import *

class PopUp(PseudoWindow):
	def __init__(self, coord = (0, 0), dim = (330, 300), color = (128, 128, 128, 1), msgId, fontColor):
		super().__init__(self, coord, dim, color)
		self.msgId = msgId
		self.fontColor = fontColor
		self.fontType = pygame.font.Font("../App/Shared/Assets/Graphics/Fonts/Square.ttf", 12)
		self.topText = pygame.Surface((self.surfContent.get_height() * 0.24), self.surfContent.get_width() * 0.85)
		self.midText = pygame.Surface((self.surfContent.get_height() * 0.24), self.surfContent.get_width() * 0.85)
		self.botText = pygame.Surface((self.surfContent.get_height() * 0.24), self.surfContent.get_width() * 0.85)

	def draw(self, fontColor):
		super().draw()

		# match self.msgId:
		# 	case 1:
		# 		self.topText.font.render()
			






# You're an idiot :)
# Get hacked back !
# Bleh you can't see
