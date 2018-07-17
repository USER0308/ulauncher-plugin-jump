import logging
import os

# logger = logging.getLogger()



class List_choice():
    '''List the most frequency used location in file system'''

    def check_exist(self,database_path):
        '''check the path exists'''
        if not os.path.exists(database_path):
            #logger.warn('database.txt not exists, creating')
            print "%s not exists, creating" % database_path
            f = open(database_path,"w")
            f.close()
            #logger.info('create database.txt')


    def get_top_five(self,path):
        '''get the top five most frequency path'''
        print "calling get top five"
        database_path = "database.txt"
        print "current path is %s " % os.getcwd()
        self.check_exist(database_path)
        f = open(database_path,'r')  # open for read
        print f
        records = []
        for line in f:
            print "lines are %s in database" % line
            line=line.strip('\n')
            record_list = line.split(" ")
            records.append(record_list)
        f.close()
        print records
        #logger.debug('database.txt content is:===================')
        for record in records:
            print record[0],record[1]

        # check if path exists
        contain_records = []
        for record in records:
            if path in record[0]:
                #logger.debug('find a record')
                contain_records.append(record)

        # sort the record and take the first five
        contain_records = sorted(contain_records, key=lambda x:x[1], reverse = True)
        print contain_records
        #logger.debug('first five are:')
        end_point = 5 if len(contain_records)>=5 else len(contain_records)
        for i in range(0,end_point):
            record = contain_records[i]
            print record[0],record[1] 
        return contain_records[0:6]

    def write_path(self,path):
        '''write a new one or increase the weight'''
        database_path = "database.txt"
        tmp_path = "tmp"
        self.check_exist(database_path)
        self.check_exist(tmp_path)
        print "open file to write"
        read_file = open(database_path, 'r')  # open for write
        write_file = open(tmp_path,"w")  # open for write
        for line in read_file:
            line=line.strip('\n')
            record_list = line.split(" ")
            if path == record_list[0]:
                print "file name in current record"
                record_list[1] = str(int(record_list[1])+1)
                new_record = record_list[0] + " " + record_list[1] + "\n"
                print new_record
                write_file.write(new_record)
                write_file.flush()
            else:
                line = line + "\n"
                write_file.write(line)
                write_file.flush()
        read_file.close()
        write_file.close()
        os.remove(database_path)
        os.rename(tmp_path,database_path)
        print "write path finish"


if __name__ == '__main__':
    List_choice().get_top_five('/home')
    List_choice().write_path('/home')