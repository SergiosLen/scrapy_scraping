require 'json'

input_dir=''
filepaths = Dir.glob(input_dir+'**/*.json')
# p filepaths
raise 'No .json files found!!!!' if filepaths.empty?

filepaths.each do |filepath|
    doc= File.read(filepath) #do |ddoc|
        # p ddoc
        data_hash = JSON.parse(doc)
        # p data_hash.keys()
        data_hash.each do |u|
            # p u, u.keys,u['links']
            # File.open(input_dir+'links.txt','a+') {|ff| ff.write(u['link']+"\n")}
            File.open(input_dir+'report.txt','a+') {|ff| ff.write(u['created'][0]+"\n" + u['title'][0]+"\n"+u['desc'][0]+"\n" + u['link']+"\n" +'==========================================================='+"\n")}

            # p u[]
            # fop.write(data_hash['link']+"\n")
            # ffop.write()
        end 

    # end
end
# fop = File.open(input_dir+'links.txt','w')
# ffop= File.open(input_dir+'report.txt','w')
  