#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>

#include <iostream>
typedef unsigned char BYTE;
typedef unsigned long DWORD;


int main()
{
	cv::Mat img;

	img = cv::imread("C:\\Users\\rbucur\\source\\repos\\Project10\\Project10\\decriptare.png",1);
	//std::cout << img;
	//return 0;
	DWORD x = 0;
	DWORD y = 0;

	std::string mesaj_rezultat;
	
	BYTE octet_rezultat = 0;
	DWORD MASK = 0x01;
	DWORD counter = 8;
	BYTE octet;


	
	BYTE* ptr_to_end = &img.at<BYTE>(0, 0);
		
	for (y = 0; y < img.rows; ++y)
	{
		for (x = 0; x < img.cols; x+=3)
		{
			if (counter != 0)
			{
				octet = img.at<BYTE>(y, x) & MASK;
				octet = octet << (counter - 1);
				octet_rezultat = octet_rezultat | octet;
				counter--;
		
				if (*ptr_to_end == 'R' && *(ptr_to_end + 1) == 'C' && *(ptr_to_end + 2) == 'T')
				{
					goto end;
				}
				ptr_to_end += 3;
				//std::cout << (int)octet_rezultat << " ";
				if (counter == 0)
				{
					
					counter = 8;
					mesaj_rezultat += octet_rezultat;
					octet_rezultat = 0;
					
				}
			}
		}
		std::cout << '\n';
	}

	end:
	std::cout << '\n';
	std::cout << mesaj_rezultat;
	cv::namedWindow("Display window", cv::WINDOW_AUTOSIZE); // Create a window for display.
	cv::imshow("Display window", img);
	cv::waitKey(0);
	return 0;
}