from PIL import Image

from histogram import histogram

class histogram_attack:

    def histogram_difference(self, first_hist, second_hist):
        if len(first_hist) != len(second_hist):
            raise Exception("Histogram shapes should match")
        
        hist_diff = []
        for ind in range(len(first_hist)):
            hist_diff.append(first_hist[ind] - second_hist[ind])
        
        return hist_diff
    
    def attack(self):
        cover_image_hist = histogram(self.cover_image)
        suspicious_image_hist = histogram(self.suspicious_image)

        [cover_image_r_hist, cover_image_g_hist, cover_image_b_hist] = cover_image_hist.compute_histogram()
        [suspicious_image_r_hist, suspicious_image_g_hist, suspicious_image_b_hist] = suspicious_image_hist.compute_histogram()

        self.diff_r_hist = self.histogram_difference(cover_image_r_hist, suspicious_image_r_hist)
        self.diff_g_hist = self.histogram_difference(cover_image_g_hist, suspicious_image_g_hist)
        self.diff_b_hist = self.histogram_difference(cover_image_b_hist, suspicious_image_b_hist)
    
    def _analyze_pattern(self, diff):
        ind = 0
        count_pattern = 0

        while ind < (len(diff)-1):
            if diff[ind] != 0 and diff[ind+1] != 0 and diff[ind] + diff[ind+1] == 0:
                count_pattern += 1
            ind += 2
        
        return count_pattern

    def analyze(self):
        count_r = self._analyze_pattern(self.diff_r_hist)
        count_g = self._analyze_pattern(self.diff_g_hist)
        count_b = self._analyze_pattern(self.diff_b_hist)

        if count_r >= self.threshold and count_g >= self.threshold and count_b >= self.threshold:
            return True
        return False

    def __init__(self, cover_image_path, suspicious_image_path):
        # if pattern is found >= threshold value, it is a stego image
        self.threshold = 60

        self.cover_image = Image.open(cover_image_path)
        self.suspicious_image = Image.open(suspicious_image_path)
