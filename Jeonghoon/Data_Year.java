import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Data_Year {
	public static void main(String[] args) throws IOException {
		List<List<String>> ret = new ArrayList<List<String>>();
		BufferedReader br = null;
		BufferedReader br_join = null;
		BufferedWriter brwrite = null;
		try {
			br = Files.newBufferedReader(Paths.get("C:\\Users\\Baek\\Desktop\\SK데이터분석\\맥북\\train.csv"));
			br_join = Files
					.newBufferedReader(Paths.get("C:\\Users\\Baek\\Desktop\\SK데이터분석\\맥북\\train_display_real.csv"));
			brwrite = Files.newBufferedWriter(Paths.get("C:\\Users\\Baek\\Desktop\\SK데이터분석\\맥북\\complete.csv"));
			String line = "";
			String line_join = "";
			while ((line = br.readLine()) != null && (line_join = br_join.readLine()) != null) {
				System.out.println(line);
				// CSV 1행을 저장하는 리스트
				List<String> tmpList = new ArrayList<String>();
				List<String> tmpList_join = new ArrayList<String>();
				String array[] = new String[12];
				String array_join[] = new String[12];
				int commacnt = 0;
				for (int i = 0; i < line.length(); i++) {
					if (line.charAt(i) == ',') {
						commacnt++;
					}
				}

				if (commacnt == 11) {
					array = line.split(",");
					array_join = line_join.split(",");
				} else {
					int tempcnt = 0;
					int index = 0;
					for (int i = line.length() - 1; i > -1; i--) {
						if (line.charAt(i) == ',') {
							tempcnt++;
						}
						if (tempcnt == 10) {
							index = i;
							break;
						}
					}
					int tempcnt_join = 0;
					int index_join = 0;
					for (int i = line_join.length() - 1; i > -1; i--) {
						if (line_join.charAt(i) == ',') {
							tempcnt_join++;
						}
						if (tempcnt_join == 10) {
							index_join = i;
							break;
						}
					}
					String temps = line.substring(index + 1, line.length());
					String temps_join = line_join.substring(index_join + 1, line_join.length());
					array[0] = line.substring(0, index);
					array_join[0] = line_join.substring(0, index_join);
					
					for (int i = 0; i < array[0].length(); i++) {
						if (array[0].charAt(i) == ',') {
							array[1] = array[0].substring(i + 1, array[0].length());
							array[0] = array[0].substring(0, i);
							break;
						}
					}
					
					for (int i = 0; i < array_join[0].length(); i++) {
						if (array_join[0].charAt(i) == ',') {
							array_join[1] = array_join[0].substring(i + 1, array_join[0].length());
							array_join[0] = array_join[0].substring(0, i);
							break;
						}
					}
					
					String back[] = temps.split(",");
					String back_join[] = temps_join.split(",");
					for (int i = 0; i < 10; i++) {
						array[i + 2] = back[i];
						array_join[i + 2] = back_join[i];
					}
				}
				String temp = array[1];
				array[1] = array[1].toUpperCase(); // 임시로 전부 대문자로 변환
				int year = array.length - 4;
				for (int i = 0; i < array.length; i++) {
					if (i == 1) {
						// 제목에서의 연도에 따라 자동매핑

						if (array[1].contains("2009")) {
							array[year] = "2009";
						} else if (array[1].contains("2010")) {
							array[year] = "2010";
						} else if (array[1].contains("2011")) {
							array[year] = "2011";
						} else if (array[1].contains("2012")) {
							array[year] = "2012";
						} else if (array[1].contains("2013")) {
							array[year] = "2013";
						} else if (array[1].contains("2014")) {
							array[year] = "2014";
						} else if (array[1].contains("2015")) {
							array[year] = "2015";
						} else if (array[1].contains("2016")) {
							array[year] = "2016";
						} else if (array[1].contains("2017")) {
							array[year] = "2017";
						} else if (array[1].contains("2018")) {
							array[year] = "2018";
						} else if (array[1].contains("2019")) {
							array[year] = "2019";
						} else if (array[1].contains("2020")) {
							array[year] = "2020";
						} else if (array[1].contains("MWTJ2KH")) {
							array[year] = "2020";
						} else if (array[1].contains("MVFL2KH")) {
							array[year] = "2020";
						} else if (array[1].contains("M1")) {
							array[year] = "2020";
						} else if (array[1].contains("MC965LL")) {
							array[year] = "2012";
						} else if (array[1].contains("MD711LL")) {
							array[year] = "2014";
						} else if (array[1].contains("MJVM2LL")) {
							array[year] = "2016";
						} else if (array[1].contains("MD761LL")) {
							array[year] = "2015";
						} else if (array[1].contains("MD223LL")) {
							array[year] = "2013";
						} else if (array[1].contains("9세대")) {
							array[year] = "2019";
						} else if (array[1].contains("I9-9980HK")) {
							array[year] = "2019";
						} else if (array[1].contains("I9-9880H")) {
							array[year] = "2019";
						} else if (array[1].contains("I7-9750H")) {
							array[year] = "2020";
						} else if (array[1].contains("I7-1068NG7")) {
							array[year] = "2020";
						} else if (array[1].contains("I5-1038NG7")) {
							array[year] = "2020";
						} else if (array[1].contains("I7-8557U")) {
							array[year] = "2020";
						} else if (array[1].contains("I5-8257U")) {
							array[year] = "2020";
						} else if (array[1].contains("I9-9880H")) {
							array[year] = "2020";
						} else if (array[1].contains("I7-9750H")) {
							array[year] = "2020";
						} else if (array[1].contains("I7-8557U")) {
							array[year] = "2019";
						} else if (array[1].contains("I5-8257U")) {
							array[year] = "2019";
						} else if (array[1].contains("I9-9880H")) {
							array[year] = "2019";
						} else if (array[1].contains("I7-9750H")) {
							array[year] = "2019";
						} else if (array[1].contains("I7-8569U")) {
							array[year] = "2019";
						} else if (array[1].contains("I5-8279U")) {
							array[year] = "2019";
						} else if (array[1].contains("I5-8") || array[1].contains("I7 8")) {
							array[year] = "2018";
						} else if (array[1].contains("I7-8") || array[1].contains("I7 8")) {
							array[year] = "2018";
						} else if (array[1].contains("I9-8") || array[1].contains("I7 8")) {
							array[year] = "2018";
						} else if (array[1].contains("I7-7") || array[1].contains("I7 7")) {
							array[year] = "2017";
						} else if (array[1].contains("I5-7") || array[1].contains("I5 7")) {
							array[year] = "2017";
						} else if (array[1].contains("I7-6") || array[1].contains("I7 6")) {
							array[year] = "2016";
						} else if (array[1].contains("I5-6") || array[1].contains("I5 6")) {
							array[year] = "2016";
						} else if (array[1].contains("I7-4") || array[1].contains("I7 4")) {
							array[year] = "2014";
						} else if (array[1].contains("I7-5") || array[1].contains("I7 5")) {
							array[year] = "2015";
						} else if (array[1].contains("I5-5") || array[1].contains("I5 5")) {
							array[year] = "2015";
						} else if (array[1].contains("I5-4") || array[1].contains("I5 4")) {
							array[year] = "2014";
						} else if (array[1].contains("I7-3") || array[1].contains("I7 3")) {
							array[year] = "2013";
						} else if (array[1].contains("I5-3") || array[1].contains("I5 3")) {
							array[year] = "2013";
						} else if (array[1].contains("I7-2") || array[1].contains("I7 2")) {
							array[year] = "2011";
						} else if (array[1].contains("MY")) {
							array[year] = "2020";
						} else if (array[1].contains("MW")) {
							array[year] = "2020";
						} else if (array[1].contains("MX")) {
							array[year] = "2020";
						} else if (array[1].contains("MV")) {
							array[year] = "2019";
						} else if (array[1].contains("MU")) {
							array[year] = "2019";
						} else if (array[1].contains("MR")) {
							array[year] = "2018";
						} else if (array[1].contains("MP")) {
							array[year] = "2017";
						} else if (array[1].contains("ML")) {
							array[year] = "2016";
						} else if (array[1].contains("MJ")) {
							array[year] = "2015";
						} else if (array[1].contains("MF")) {
							array[year] = "2015";
						} else if (array[1].contains("MG")) {
							array[year] = "2014";
						} else if (array[1].contains("ME")) {
							array[year] = "2013";
						} else if (array[1].contains("MD")) {
							array[year] = "2012";
						} else if (array[1].contains("MC")) {
							array[year] = "2012";
						} else if (array[1].contains("MD223LL")) {
							array[year] = "2013";
						} else if (array[1].contains("MD223LL")) {
							array[year] = "2013";
						} else if (array[1].contains("MD223LL")) {
							array[year] = "2013";
						} else if (array[1].contains("MD223LL")) {
							array[year] = "2013";
						} else if (array[1].contains("세대")) {
							for (int k = 0; k < array[1].length(); k++) {
								if (array[1].charAt(k) == '세') {
									int tempval = 2010 + (int) (array[1].charAt(k - 1) - 48);
									array[year] = String.valueOf(tempval);
								}
							}
						}

					}
					if (i == 1) { // 다시 원래 값 주입
						array[1] = temp;
					}
					if (i == 2) {
						brwrite.write(array_join[i]);
					} else {
						brwrite.write(array[i]);
					}
					if (i != array.length - 1) {
						brwrite.write(",");
					}
				}
				brwrite.newLine();
				// 배열에서 리스트 반환
				tmpList = Arrays.asList(array);
//				if (array[year] == "empty") {
//					System.out.println(tmpList);
//				}
				ret.add(tmpList);
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null) {
					br.close();
					br_join.close();
					brwrite.close();
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

	}
}
