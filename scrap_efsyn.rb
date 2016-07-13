require 'nokogiri'

html_path=''
html_npath=File.join(html_path,'**/*.html')
filepaths = Dir.glob(html_npath)
raise 'No .html files found!!!!' if filepaths.empty?
outputdirectory=''
Dir.mkdir outputdirectory unless File.exists? outputdirectory

# full_search_names=Array.new
# list_of_tweets=Array.new
# hash_of_tweets = Hash.new 
filepaths.each do |filepath|

# filepath = '/home/sergios-len/Downloads/dim/aisiodoxos-o-kostelo-gia-tin-axiologisi.html'
    p filepath
    doc= File.open(filepath) { |f| Nokogiri::HTML(f)}

# doc.at_xpath('/html/body/div[2]/div[6]/div/div/div/div[1]/div/div[1]/div/div/div')

    title =doc.at_xpath('/html/body/div[2]/div[6]/div/div/div/div[1]/div/div[1]/div/div/div/h1')
    date= doc.at_xpath('/html/body/div[2]/div[6]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]')
    creator=doc.at_xpath('/html/body/div[2]/div[6]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[3]')
# body
    # p date.content
    # p date.content.split[0].chomp(',')
    # p title.content
    #  p title.content.gsub('/','_')
    # p aaa
    # if 
    keim=doc.at_xpath('/html/body/div[2]/div[6]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[4]/div/div')
    if keim.nil?
    keim=doc.at_xpath('/html/body/div[2]/div[6]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[3]/div') 
    end
    ddirnam=outputdirectory + "/#{title.content.gsub('/','_').split().join('_')}_#{date.content.split[0].chomp(',')}.txt"
    File.open(ddirnam, 'w') do |file| 
        # p ddirnam
        file.write(title.content)
        file.write("\n\n")
        file.write(keim.content) 
        file.write("\n")
        file.write(creator.content)
        file.write("\n")
        file.write(date.content)
        # file.write(creator.content)
    end



end

# fop